#!/usr/bin/python
#-=- encoding: latin-1 -=-

# MÓDULOS
import cgi, cgitb, Cookie, os, base64, random, datetime
from sql_comandos.bd_select_login import bd_select_login
from sql_comandos.bd_insert_update import bd_insert_update
from sql_comandos.bd_select_smtp import bd_select_smtp
from sql_comandos.envia_email import envia_email


# FORM STORAGE
form = cgi.FieldStorage()
# COOKIE
cookie = Cookie.SimpleCookie()
cookie['expires_at_time'] = 'cookie_value'
expires = datetime.datetime.now() + datetime.timedelta(minutes=5)
cookie['expires_at_time']['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S GMT;')
# BT ENTRAR
try:
	if form.getvalue('entrar'):
		encoded = base64.b64encode(form.getvalue('passuser'))
		senha = bd_select_login("select senha from login where usuario='%s'" %form.getvalue('nomeuser'))
		if (encoded == senha):
			perfil = bd_select_login("select perfil from login where usuario='%s'" %form.getvalue('nomeuser'))
			sessao = '%s-%s' %(perfil,random.randint(1,10000) ** 2)
			bd_insert_update("update login set cookie='%s' where usuario='%s'" %(sessao,form.getvalue('nomeuser')))
			print "Set-Cookie:%s;" %sessao
			print cookie.output()
		else:
			resposta = "<script>alert('Login/Senha incorrera')</script>"
except Exception, e:
	resposta = "<script>alert('Falta de dados para BD ou BD offline')</script>"
	
# BT SAIR	
try:
	if form.getvalue('sair'):
		cookie_string = os.environ.get('HTTP_COOKIE')
		sessao = '%s' %random.randint(1,10000) ** 2
		bd_insert_update("update login set cookie='%s' where cookie='%s'" %(sessao,cookie_string))
except Exception, e:
	resposta = "<script>alert('Erro ao conectar no servidor de email')</script>"	

# BT EMAIL		
try:
	if form.getvalue('bt_email'):		
		if (bd_select_smtp("select senha from login where email='%s'" %form.getvalue('email'))):
			envia_email(form.getvalue('email'),\
			base64.b64decode(bd_select_smtp("select senha from login where email='%s'" %form.getvalue('email'))))
		else:
			resposta = "<script>alert('Email incorreto')</script>"
except Exception, e:
	resposta = "<script>alert('Email incorreto')</script>"	

# HTML
print 'Content-Type: text/html\r\n'
print """
<html>
<head>
<title>Painel</title>
<body>
<style>
body {
	background-color:#1C1C1C;
	}
	
	.border {border-style:solid;}
	.copy, .copy a {width: 660px; margin:0 auto; color: #DD8888;}
	.formresult {background-color:#FFFF99;display:block;padding:10px;}
	.seletor {font-family: Verdana, Sans-Serif; font-size:5px;} 

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
<hr>
<h2><font color="#FFFFFF"><center>Dhcp Web 2.0</center></font></h2>
<hr>
<form  method="POST">
<table align="center" border="0" width='200'>
        <tr>
        		<td  align="center" ><font color="#FFFFFF"><br />Login</font></td>
        		<td  align="center" width="25"><br /><input type="text"  size=17 name="nomeuser"></td>
        </tr>
        <tr>
        		<td  align="center" ><font color="#FFFFFF">Senha</font></td>
        		<td  align="center" width="25"><input type="password" size=17 name="passuser"></td>      	
        	</tr>
        	<tr>
        		<td  align="center"></td>
        		<td  align="center" width="25"><input class="btn" type="submit" value="Entrar" name="entrar"> <input class="btn" type="submit" value="Sair" name="sair" onclick="window.top.location=window.top.location;"><br /></td>
			</tr> 	
        </tr>
			<tr>
				<td align="center"></td>	
				<td align="center" width="25"><font color="#FFFFFF">Recuperar Senha</font></td>	
			</tr>
			<tr>	
        		<td  align="center" width="25"><font color="#FFFFFF">Email</font></td> 		
        		<td  align="center"><input type="text" size=20 name="email"></td>
        	</tr>
        	<tr>
        		<td align="center"></td>
        		<td  align="center" width="25"><input class="btn" type="submit" value="Enviar" name="bt_email"><br /></td>
			</tr>
</table>
<br />
	<table align="left" border="0">
		<tr><td align="left">
			<a href="administracao.py" target="centro"><font color="#FFFFFF"><br />ADMINISTRA&Ccedil;&Atilde;O</a></font></td></tr>
		<tr><td align="left">
			<a href="admhosts.py" target="centro"><font color="#FFFFFF">CADASTRO</font></td></tr>
		<tr><td align="left">
			<a href="admconf.py" target="centro"><font color="#FFFFFF">DHCP.CONF</font></td></tr>
		<tr><td align="left">
			<a href="listarip.py" target="centro"><font color="#FFFFFF">HOSTS ATIVOS</font></td></tr>		
		<tr><td align="left">
			<a href="removeip.py" target="centro"><font color="#FFFFFF">REMOVER HOSTS</font><br /></td></tr>
		<tr><td align="left">
			<a href="servidor.py" target="centro"><font color="#FFFFFF">SERVIDOR</font><br /><br /></td></tr>	
	</table>
</form>
</body>
</head>
</html>
"""
print resposta
