#!/usr/bin/python
#-=- encoding: latin-1 -=-

# IMPORTANDO OS MÓDULOS
import cgi, cgitb, Cookie, os, time, re, datetime
from sql_comandos.bd_ins_del_upd import bd_ins_del_upd
from sql_comandos.bd_select_grupo import bd_select_grupo
from sql_comandos.bd_select_ipdisp import bd_select_ipdisp
from sql_comandos.bd_select_login import bd_select_login

# RECEBENDO O COOKIE
print 'Content-Type: text/html\n'
cookie = Cookie.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
cookie_string = cookie_string.split(' ')[0].replace(';','')
valid_cookie = bd_select_login("select cookie from login where cookie='%s'" %cookie_string)
# VALIDANDO O COOKIE
if (cookie_string != valid_cookie):
	print  "<script>self.location.href='manual.py';</script>"

# FORM STORAGE
form = cgi.FieldStorage() 

# CADASTRO DO GRUPO-IP
try:
	if form.getvalue('bt_cad_grupo'):
		if form.getvalue('add_grupo'):
			bd_ins_del_upd("insert into grupo (nome_grupo) values ('%s')" %form.getvalue('add_grupo'))
except Exception, e:
	resposta = "<script>alert('Grupo cadastrado anteriormente')</script>"
	
# REMOVER GRUPO-IP
try:
	if form.getvalue('bt_rem_grupo'):
		bd_ins_del_upd("delete from grupo where nome_grupo='%s'" %form.getvalue('rem_grupo'))	
except Exception, e:
	resposta = "<script>alert('Verifique o Manual')</script>"
        
# CADASTRAR HOST
try:
	if form.getvalue('bt_cad_host'):
		if re.match("[0-9a-f]{2}([:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", form.getvalue('mac_address').lower()):
			bd_ins_del_upd("insert into dhcp(hostname,mac_address,ip_address,patrimonio,grupo_fk) values ('%s','%s','%s','%s','%s')" \
			%(form.getvalue('hostname'),form.getvalue('mac_address'),form.getvalue('ips'),form.getvalue('patrimonio'),form.getvalue('grupos')))
		else:
			resposta = "<script>alert('Verifique o Manual')</script>"
except Exception, e:
	resposta = "<script>alert('Verifique o Manual')</script>"    

# ALTERAR HOSTNAME	
try:
	if form.getvalue('bt_alt_hostname'):
		bd_ins_del_upd(" update dhcp set hostname='%s' where hostname='%s'" \
		%(form.getvalue("alt_hostname"),form.getvalue("sel_hostname")))
except Exception, e:
	resposta = "<script>alert('Verifique o Manual')</script>"		
	
# ALTERAR GRUPO-IP	
try:
	if form.getvalue('bt_alt_grupo'):
		bd_ins_del_upd("update dhcp set grupo_fk='%s' where grupo_fk='%s'" \
		%(form.getvalue("sel_grupo_no"),form.getvalue("sel_grupo_at")))
except Exception, e:
	resposta = "<script>alert('Verifique o Manual')</script>"
	
# ALTERAR PATRIMONIO	
try:
	if form.getvalue('bt_alt_patrimonio'):
		bd_ins_del_upd("update dhcp set patrimonio='%s' where hostname='%s'" \
		%(form.getvalue("alt_patrimonio"),form.getvalue("sel_hostname_pat")))
except Exception, e:
	resposta = "<script>alert('Verifique o Manual')</script>"
	
# RECEBENDO OS CAMPOS PARA CRIAR A SELEÇÃO
grupos 			= bd_select_grupo('nome_grupo','grupo',' ')
grupos_ativos 	= bd_select_grupo('grupo_fk','dhcp',' ')
ips	 			= bd_select_ipdisp()
hostname 		= bd_select_grupo('hostname','dhcp','order by (hostname)')
rm_grupo 		= bd_select_grupo('nome_grupo','grupo','where nome_grupo not in (select nome_grupo from grupo inner join dhcp on grupo.nome_grupo=dhcp.grupo_fk)')
patrimonio 		= bd_select_grupo('patrimonio','dhcp', 'order by (patrimonio)')

# HTML
print """
<html>
<head>
<title>Administra&ccedil;&atilde;o</title>
<body>
<style>
body {
	background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAIAAAACUFjqAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QsZDiQNvXI8RAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVBjTY/z//z8DbsDEgBcMXWmW////4pP+8+srAwPOkAEAxw8J+pT6JekAAAAASUVORK5CYII=);
	}
	
	.border {border-style:solid;}
	.copy, .copy a {width: 660px; margin:0 auto; color: #DD8888;}
	.formresult {background-color:#FFFF99;display:block;padding:10px;}
	.seletor {font-family: Arial, Sans-Serif; font-size:6px;} 

.btn {
  background: #2f3030;
  background-image: -webkit-linear-gradient(top, #2f3030, #949294);
  background-image: -moz-linear-gradient(top, #2f3030, #949294);
  background-image: -ms-linear-gradient(top, #2f3030, #949294);
  background-image: -o-linear-gradient(top, #2f3030, #949294);
  background-image: linear-gradient(to bottom, #2f3030, #949294);
  -webkit-border-radius: 3;
  -moz-border-radius: 3;
  border-radius: 3px;
  text-shadow: 1px 1px 0px #666666;
  -webkit-box-shadow: 1px 1px 5px #666666;
  -moz-box-shadow: 1px 1px 5px #666666;
  box-shadow: 1px 1px 5px #666666;
  font-family: Arial;
  color: #ffffff;
  font-size: 13px;
  padding: 1px 2px 1px 2px;
  text-decoration: none;
}

.btn:hover {
  text-decoration: none;
}
</style>
<form  method="POST">
<fieldset>
<legend>Cadastro</legend>
<table>	
	<tr><td>
			<b>Criar um Grupo-IP</b>
		</td>
	</tr>
	<tr>
		<td>
			Nome do Grupo:</td><td><input type="text" size="17" maxlength="12" name="add_grupo">
		</td>
	</tr>
	<tr>
		<td>
		</td>
		<td align="right">
			 <input class="btn" type="submit"  value="Cadastrar" name="bt_cad_grupo" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
	<tr><td>
			<b>Remover um Grupo-IP</b>
		</td>
	</tr>
	<tr>									
		<td>Grupo:</td><td><select name="rem_grupo">
							<option value="0">Selecione o Grupo-IP</option>
         				%s """ %rm_grupo
print """
							</select></td>
	</tr>
	<tr>
		<td>
		</td>
		<td align="right">
			 <input class="btn" type="submit"  value="Remover" name="bt_rem_grupo" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
	<tr>
		<td>
			<br /><b>Fixar IP Adrress</b>
		</td>
	</tr>
	<tr>
		<td>Hostname:</td><td><input type="text" size="17" maxlength="30" name="hostname"></td>
	</tr>
	<tr>
		<td>Mac address:</td><td><input type="text" size="17" maxlength="17" name="mac_address"></td>
	</tr>
	<tr>
		<td>Patrim&ocirc;nio:</td><td><input type="text" size="17" maxlength="30" name="patrimonio"></td>
	</tr>
	<tr>
		<td>Ip Address:</td><td><select name="ips">
							<option value="0">Selecione o IPadress</option>
         				%s """ %ips
print """
							</select></td>	
	</tr>
	<tr>									
		<td>Grupo:</td><td><select name="grupos">
							<option value="0">Selecione o Grupo-IP</option>
         				%s """ %grupos
print """
							</select></td>
	</tr>
	<tr>							
		<td>
		</td>
		<td align="right">
			<input class="btn" type="submit" value="Cadastrar" name="bt_cad_host" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
	<tr><td>
			<b>Alterar Patrim&ocirc;nio</b>
		</td>
	</tr>
	<tr>
		<td>
		Patrim&ocirc;nio atual:</td><td><select name="sel_patrimonio">
							<option value="0">Selecione o Hostname</option>
         				%s """ %patrimonio
print """
		</td>
		<td>
			Hostname atual:</td><td><select name="sel_hostname_pat">
							<option value="0">Selecione o Hostname</option>
         				%s """ %hostname
print """
		</td>
		<td>
			Patrim&ocirc;nio novo:</td><td><input type="text" size="17" maxlength="30" name="alt_patrimonio">
		</td>
		<td>
			<input class="btn" type="submit"  value="Alterar" name="bt_alt_patrimonio" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
	<tr><td>
			<b>Alterar Hostname</b>
		</td>
	</tr>
	<tr>
		<td>
			Hostname atual:</td><td><select name="sel_hostname">
							<option value="0">Selecione o Hostname</option>
         				%s """ %hostname
print """
		</td>
		<td>
			Hostname novo:</td><td><input type="text" size="17" maxlength="12" name="alt_hostname">
		</td>
		<td>
			<input class="btn" type="submit"  value="Alterar" name="bt_alt_hostname" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
		<tr><td>
			<b>Alterar Grupo</b>
		</td>
	</tr>
	<tr>
		<td>
			Grupo atual:</td><td><select name="sel_grupo_at">
							<option value="0">Selecione Grupo Ativo</option>
         				%s """ %grupos_ativos
print """
		</td>
		<td>
			Grupo novo:</td><td><select name="sel_grupo_no">
							<option value="0">Selecione Novo Grupo</option>
         				%s """ %rm_grupo
print """
		</td>
		<td>
			<input class="btn" type="submit"  value="Alterar" name="bt_alt_grupo" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
</table>
</fieldset>
</form>
</body>
</head>
</html>
"""
print resposta
