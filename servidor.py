#!/usr/bin/python
#-=- encoding: latin-1 -=-

# Importando os módulos 
import cgi, cgitb, Cookie, os
from sql_comandos.gerar_conf_deb import gerar_conf_deb
from sql_comandos.gerar_conf_cen import gerar_conf_cen
from sql_comandos.bd_select_login import bd_select_login
from sql_comandos.bd_select import bd_select
from sql_comandos.bd_select_arp import bd_select_arp


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

print_conf1 =''
print_conf2 =''
texto1 = 'Confirme para gerar o arquivo udhcpd.conf.<br />Em seguida ser&aacute; iniciado o servi&ccedil;o udhcpd.'
texto2 = 'Confirme para gerar o arquivo dhcpd.conf.<br />Em seguida ser&aacute; iniciado o servi&ccedil;o dhcpd.'
resposta = ''

try:
	if form.getvalue('bt_conf_deb'):
		print_conf1 = """<tr><td>%s	</td></tr><td>"""\
		%gerar_conf_deb("<br />","select mac_address,ip_address from dhcp","<br />")
		var_file=open("conf/udhcpd.conf", "w")
		var_file.write(gerar_conf_deb("","select mac_address,ip_address from dhcp",""))
		var_file.close()
		os.system("/usr/bin/sudo /bin/cp conf/udhcpd.conf /etc/")
		comando = os.system("/usr/bin/sudo /etc/init.d/udhcpd restart >> /dev/null")
     	comando = str(comando)
    	if (comando == "0"):
    		resposta = "<script>alert('Restart dhcpd: [ OK ]')</script>"
    		texto1 = "servidor iniciado com sucesso"   	
    	else:
    		resposta = "<script>alert('Restart udhcpd: [ FALHOU ]. Verifique o Conf!')</script>" 		
except Exception, e:
        log_erro = "Erro bt_conf_deb"
        
try:
	if form.getvalue('bt_conf_cen'):
		print_conf2 = """<tr><td>%s</td></tr><td>"""\
		%gerar_conf_cen("<br />","select hostname,mac_address,ip_address,grupo_fk from dhcp","<br />")
		var_file=open("conf/dhcpd.conf", "w")
		var_file.write(gerar_conf_cen("","select hostname,mac_address,ip_address,grupo_fk from dhcp","\n"))
		var_file.close()
		if (bd_select('c_caminho_conf','admconf') == '6'):
			os.system("/usr/bin/sudo /bin/cp conf/dhcpd.conf /etc/dhcp/")
			comando = os.system("/usr/bin/sudo /etc/init.d/dhcpd restart >> /dev/null")
  			comando = str(comando)
  			if (comando == "0"):
  				resposta = "<script>alert('Restart dhcpd: [ OK ]')</script>"
  				texto2 = "servidor iniciado com sucesso" 
  			else:
  				resposta = "<script>alert('Restart udhcpd: [ FALHOU ]. Verifique o Conf!')</script>"
  		else:
  			os.system("/usr/bin/sudo /bin/cp conf/dhcpd.conf /etc/")
			comando = os.system("/usr/bin/sudo /etc/init.d/dhcpd restart >> /dev/null")
  			comando = str(comando)
  			comando = str(comando)
  			if (comando == "0"):
  				resposta = "<script>alert('Restart dhcpd: [ OK ]')</script>"
  				texto2 = "servidor iniciado com sucesso"
  			else:
  				resposta = "<script>alert('Restart udhcpd: [ FALHOU ]. Verifique o Conf!')</script>"
except Exception, e:
        log_erro = "Erro bt_conf_con"			


try:
	if form.getvalue('bt_gera_arp'):
		var_file=open("conf/ethers", "w")
		var_file.write(bd_select_arp("select ip_address,mac_address from dhcp"))
		var_file.close()
		os.system("/usr/bin/sudo /sbin/arp -f conf/ethers")
		os.system("/usr/bin/sudo /usr/sbin/arp -f conf/ethers")
		resposta = "<script>alert('Arquivo gerado com sucesso')</script>"
except Exception, e:
        log_erro = "Erro bt_gera_arp"				   

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
<legend>Servidor</legend>
<table>
	<tr>
		<td>
			<h2>Tabela Arp</h2>
		</td>
	</tr>
	<tr>
		<td>
			Gerar arquivo ethers<br />OBS: O arquivos ethers deve ser gerado antes de iniciar o servidor.<br />
			<input class="btn" type="submit"  value="Confirmar" name="bt_gera_arp" onclick="return confirm('voc&ecirc; confirmar?')"/>
			<br />		
		</td>
	</tr>	
	<tr>
		<td>
			<br /><h2>Debian 7</h2>
		</td>
	</tr>
	<tr>
		<td>
			%s<br/>%s""" %(texto1,print_conf1)
print """						
		</td>
	</tr>
	<tr>
		<td>
			 <input class="btn" type="submit"  value="Confirmar" name="bt_conf_deb" onclick="return confirm('voc&ecirc; confirmar?')"/>
		</td>
	</tr>
	<tr>
		<td>
			<br /><h2>CentOS 5 e 6</h2>
		</td>
	</tr>
	<tr>
		<td>
			%s<br/>%s""" %(texto2,print_conf2)
print """						
		</td>
	</tr>
	<tr>
		<td>
			 <input class="btn" type="submit"  value="Confirmar" name="bt_conf_cen" onclick="return confirm('voc&ecirc; confirmar?')"/>
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
