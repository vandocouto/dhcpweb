#!/usr/bin/python
#-=- encoding: latin-1 -=-

# IMPORTANDO OS MÓDULOS
import cgi, cgitb, Cookie, os, time, re, base64
from sql_comandos.bd_insert_update import bd_insert_update
from sql_comandos.bd_select_smtp import bd_select_smtp
from sql_comandos.bd_select_login import bd_select_login
from sql_comandos.bd_list_users import bd_list_users


# RECEBENDO O COOKIE
cookie = Cookie.SimpleCookie()
print 'Content-Type: text/html\n'
cookie_string = os.environ.get('HTTP_COOKIE')
cookie_string = cookie_string.split(' ')[0].replace(';','')
valid_cookie = bd_select_login("select cookie from login where cookie='%s'" %cookie_string)
# VALIDANDO O COOKIE
if (cookie_string != valid_cookie):
	print  "<script>self.location.href='manual.py';</script>"
	
# FORM STORAGE
form = cgi.FieldStorage()
smtpserver = bd_select_smtp("select smtpserver from smtp")
smtpporta = bd_select_smtp("select smtpporta from smtp")
smtplogin = bd_select_smtp("select smtplogin from smtp")
smtpemail = bd_select_smtp("select smtpemail from smtp")
smtpsenha = bd_select_smtp("select smtpsenha from smtp")

# HTML PERFIL ADMINISTRADOR
if (cookie_string[0] == "1"):
	html_admin = '''<tr><h2>Configura&ccedil;&atilde;o do smtp</h2></tr>
	<tr><td>Smtp</td><td><input type="text"  size=25 name="smtpserver" value="%s">    	
    		Porta <input type="text"  size=5 name="smtpporta" value="%s"></td></tr>
    	<tr><td>Login</td><td><input type="text"  size=25 name="smtplogin" value="%s"></td></tr>
    	<tr><td>Email</td><td><input type="text"  size=25 name="smtpemail" value="%s"></td></tr>   	
    	<tr><td>Senha</td><td><input type="password"  size=25 name="smtpsenha"></td></tr>
    	<tr><td><input class="btn" type="submit" value="Confirmar" name="smtp_confirme"><br /><br /></td></tr>
   <tr><td><h2>Cadastro de usu&aacute;rio</h2></td></tr>
   	<tr><td>Administrador</td><td>Sim<input type="radio" name="perfil" value="1">
    	N&atilde;o<input type="radio" name="perfil" value="2"></td></tr>
    	<tr><td>Login</td><td><input type="text" size=25 maxlength="15" name="c_login"></td></tr>
    	<tr><td></td><td>*** M&aacute;ximo de 10 caracteres</td></tr>
    	<tr><td>Senha Nova</td><td><input type="password"  size=25 maxlength="10" name="cs_nova1"></td></tr>
    	<tr><td>Senha Nova</td><td><input type="password"  size=25 maxlength="10" name="cs_nova2"></td></tr>
    	<tr><td>Email</td><td><input type="text"  size=25 name="cs_email"></td></tr>    	
	<tr><td>Todos os campos s&atilde;o obrigat&oacute;rios</center></td></tr>
	<tr><td><input class="btn" type="submit" value="Cadastrar" name="cad_confirme"><br /><br /></td></tr>
	<tr><td><h2>Remover usu&aacute;rio</h2></td></tr>
   <tr><td>Usu&aacute;rio</td><td><select name="users">
							<option value="0">Selecione</option>
							%s
							</tr>
	<tr><td><input class="btn" type="submit" value="Remover" name="rem_confirme" onclick="return confirm(\'voc&ecirc; confirmar?\')"><br /><br /></td></tr>
	''' %(smtpserver,smtpporta,smtplogin,smtpemail,bd_list_users())
else:
	html_admin = ''

# SMTP
try:
	if form.getvalue('smtp_confirme'):
		bd_insert_update("update smtp set smtpserver='%s',smtpporta='%s',smtplogin='%s',smtpemail='%s',smtpsenha='%s' where id='1'" \
		%(form.getvalue('smtpserver'),form.getvalue('smtpporta'),form.getvalue('smtplogin'),form.getvalue('smtpemail'),form.getvalue('smtpsenha')))
		resposta = "<script>self.location.href='administracao.py';</script>"
except Exception, e:
	resposta = "<script>alert('Erro - Verifique o manual')</script>"

# CASDASTRO DE USUÁRIO
try:
	if form.getvalue('cad_confirme'):
		if (form.getvalue('cs_nova1') == form.getvalue('cs_nova2')):
			bd_insert_update("insert into login (perfil,usuario,senha,cookie,email) values ('%s','%s','%s','0','%s')" \
			%(form.getvalue('perfil'),form.getvalue('c_login'),base64.b64encode(form.getvalue('cs_nova2')),form.getvalue('cs_email')))
			resposta  = "<script>alert('Adicionado com Sucesso')</script>"
			resposta += "<script>self.location.href='administracao.py';</script>"
		else:
			resposta = "<script>alert('Senhas diferentes')</script>"
except Exception, e:
	resposta = "<script>alert('Erro - Verifique o manual')</script>"
	
# REMOVENDO USUÁRIO
try:
	if (form.getvalue('rem_confirme') and \
	form.getvalue('users') != 'admin'):
		bd_insert_update("delete from login where usuario like '%s'" %form.getvalue('users'))
		resposta = "<script>self.location.href='administracao.py';</script>"
except Exception, e:
	resposta = "<script>alert('Erro - Verifique o manual')</script>"	
				

# TROCA DE SENHA
try:
	if form.getvalue('ts_confirme'):
		if (form.getvalue('ts_nova1') == form.getvalue('ts_nova2') and \
		(base64.b64encode(form.getvalue('ts_atual')) == bd_select_smtp("select senha from login where usuario='%s'" \
		%form.getvalue('t_login')) and (form.getvalue('ts_nova2') != form.getvalue('t_login')))):
				senha = base64.b64encode(form.getvalue('ts_nova2'))
				bd_insert_update("update login set senha='%s' where usuario='%s' and cookie='%s'" \
				%(senha,form.getvalue('t_login'),cookie_string))
				resposta = "<script>alert('Sucesso')</script>"
		else: 
			resposta = "<script>alert('Erro - Verifique o manual')</script>"
except Exception, e:
	resposta = "<script>alert('Erro - Verifique o manual')</script>"					

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
<legend>Administra&ccedil;&atilde;o</legend>
<table align="left" border="0" style="border: none;">
	%s""" %html_admin
print """	
	<tr><td><h2>Alterar senha</h2></td></tr>
    	<tr><td>Login</td><td><input type="text"  size=25 maxlength="15" name="t_login"></td></tr>
    	<tr><td>Senha Atual</td><td><input type="password"  size=25 name="ts_atual"></td></tr>
		<tr><td></td><td>*** M&aacute;ximo de 10 caracteres</td></tr>    	
    	<tr><td>Senha Nova</td><td><input type="password"  size=25 maxlength="10"  name="ts_nova1"></td></tr>
    	<tr><td>Senha Nova</td><td><input type="password"  size=25 maxlength="10" name="ts_nova2"></td></tr>
    	<tr><td><left>Todos os campos s&atilde;o obrigat&oacute;rios</center></td></tr>
    	<tr><td><input class="btn" type="submit" value="Confirmar" name="ts_confirme"></td></tr>
</table>
</fieldset>
</form>
</head>
</html>
</body>
"""
print resposta

