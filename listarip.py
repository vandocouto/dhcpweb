#!/usr/bin/python
#-=- encoding: latin-1 -=-

# IMPORTANDO OS MÓDULOS
import cgi, cgitb, Cookie, os, re
import datetime
from sql_comandos.bd_ins_del_upd import bd_ins_del_upd
from sql_comandos.bd_list_ip import bd_list_ip
from sql_comandos.bd_select_login import bd_select_login

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

# GERANDO O SELECT DE ORDERNAÇÃO
ordenacao = bd_list_ip("select hostname,mac_address,ip_address,grupo_fk,patrimonio from dhcp order by inet_aton (ip_address)")
try:
	if form.getvalue('hostname'): 
		ordenacao = bd_list_ip("select hostname,mac_address,ip_address,grupo_fk,patrimonio from dhcp order by (hostname)")
	if form.getvalue('mac_address'): 
		ordenacao = bd_list_ip("select hostname,mac_address,ip_address,grupo_fk,patrimonio from dhcp order by (mac_address)")
	if form.getvalue('ip_address'): 
		ordenacao = bd_list_ip("select hostname,mac_address,ip_address,grupo_fk,patrimonio from dhcp order by inet_aton (ip_address)")
	if form.getvalue('grupo_fk'): 
		ordenacao = bd_list_ip("select hostname,mac_address,ip_address,grupo_fk,patrimonio from dhcp order by (grupo_fk)")
except Exception, e:
	log_erro = "Error ao conectar no BD"	
	

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
  background: #090a0a;
  background-image: -webkit-linear-gradient(top, #090a0a, #2980b9);
  background-image: -moz-linear-gradient(top, #090a0a, #2980b9);
  background-image: -ms-linear-gradient(top, #090a0a, #2980b9);
  background-image: -o-linear-gradient(top, #090a0a, #2980b9);
  background-image: linear-gradient(to bottom, #090a0a, #2980b9);
  -webkit-border-radius: 28;
  -moz-border-radius: 28;
  border-radius: 28px;
  -webkit-box-shadow: 0px 1px 3px #666666;
  -moz-box-shadow: 0px 1px 3px #666666;
  box-shadow: 0px 1px 3px #666666;
  font-family: Arial;
  color: #FFFFFF;
  font-size: 17px;
  padding: 0px 8px 0px 8px;
  text-decoration: none;
}

.btn {
  -webkit-border-radius: 5;
  -moz-border-radius: 5;
  border-radius: 5px;
  -webkit-box-shadow: 0px 0px 2px #666666;
  -moz-box-shadow: 0px 0px 2px #666666;
  box-shadow: 0px 0px 2px #666666;
  font-family: Arial;
  color: #0a0a0a;
  font-size: 13px;
  padding: 5px;
  background: #ebce15;
  text-decoration: none;
}

.btn:hover {
  text-decoration: none;
}
.btn2 {
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0px;
  font-family: Arial;
  color: #0a0a0a;
  font-size: 15px;
  padding: 10px;
  background: #ebce15;
  text-decoration: none;
}

.btn2:hover {
  text-decoration: none;
}
</style>
<form  method="POST">
<fieldset>
<legend>Host Ativos</legend>
<table class="border" align="center" valign="top" width="600">
	<tr>
		<td align="center" width="120" bgcolor='#EEC900'><input class="btn2" type="submit" size="15" name="hostname" value="Hostname"></td>		
		<td align="center" width="120" bgcolor='#EEC900'><input class="btn2" type="submit" size="15" name="mac_address" value="Mac_address"></td>		
		<td align="center" width="120" bgcolor='#EEC900'><input class="btn2" type="submit" size="15" name="ip_address" value="IP_address"></td>
		<td align="center" width="120" bgcolor='#EEC900'><input class="btn2" type="submit" size="15" name="grupo_fk" value="Grupo-IP"></td>
		<td align="center" width="120" bgcolor='#EEC900'><input class="btn2" type="submit" size="15" name="patrimonio" value="Patrim&ocirc;nio"></td>		
	</tr>%s""" %ordenacao
print """ 
</table>
</fieldset>
</form>
</body>
</head>
</html>
"""
