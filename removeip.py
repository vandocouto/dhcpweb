#!/usr/bin/python
#-=- encoding: latin-1 -=-

# Importando os módulos 
import cgi, cgitb, Cookie, os, re
import datetime
from sql_comandos.bd_ins_del_upd import bd_ins_del_upd
from sql_comandos.bd_select_login import bd_select_login

# Pegando o cookie
cookie = Cookie.SimpleCookie()
print 'Content-Type: text/html\n'
cookie_string = os.environ.get('HTTP_COOKIE')
cookie_string = cookie_string.split(' ')[0].replace(';','')
valid_cookie = bd_select_login("select cookie from login where cookie='%s'" %cookie_string)
# Validando o cookie
if (cookie_string != valid_cookie):
	print  "<script>self.location.href='manual.py';</script>"

# FielStorage 
form = cgi.FieldStorage() 


try:
	if form.getvalue('bt_remover'):
		bd_ins_del_upd("delete from dhcp where mac_address like '%s'" %form.getvalue('del_mac_address'))
		resposta = "<script>alert('Removido com sucesso')</script>"
except Exception, e:
	log_erro = "Erro bt_remover"			

try:
	if form.getvalue('bt_bloquear'):
		os.system("/usr/bin/sudo /usr/sbin/arp -s %s 00:00:00:00:00:00" %form.getvalue('bloq_host')) 
		os.system("/usr/bin/sudo /sbin/arp -s %s 00:00:00:00:00:00" %form.getvalue('bloq_host')) 
		resposta = "<script>alert('Bloqueado com sucesso')</script>"
except Exception, e:
	log_erro = "Erro bt_bloquear"	
	
try:
	if form.getvalue('bt_liberar'):
		os.system("/usr/bin/sudo /usr/sbin/arp -d %s" %form.getvalue('bloq_host')) 
		os.system("/usr/bin/sudo /sbin/arp -d %s" %form.getvalue('bloq_host')) 
		resposta = "<script>alert('Liberado com sucesso')</script>"
except Exception, e:
	log_erro = "Erro bt_liberar"		


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
<legend>Remover Hosts</legend>
<table>	
	<tr><td>
			<b>Remover Host</b>
		</td>
	</tr>
	<tr>
		<td>
			Mac address:</td><td><input type="text" size="17" maxlength="17" name="del_mac_address">
		</td>
		<td>
		</td>
		<td align="right">
			 <input class="btn" type="submit"  value="Remover" name="bt_remover" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
	<tr><td><b>Bloquear Host na Tabela Arp</b>
		</td>
	</tr>
	<tr>
		<td>
			IP address:</td><td><input type="text" size="17" maxlength="15" name="bloq_host">
		</td>
		<td>
		</td>
		<td align="right">
			 <input class="btn" type="submit"  value="Bloquear" name="bt_bloquear" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
		<td align="right">
			 <input class="btn" type="submit"  value="Liberar" name="bt_liberar" onclick="return confirm('voc&ecirc; confirmar?')"/>
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
