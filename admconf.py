#!/usr/bin/python
#-=- encoding: latin-1 -=-

# Importando os módulos 
import cgi, cgitb, Cookie, os, MySQLdb
import datetime
from sql_comandos.bd_select_admconf import bd_select_admconf
from sql_comandos.bd_select import bd_select
from sql_comandos.bd_update import bd_update
from sql_comandos.bd_replace import bd_replace
from sql_comandos.bd_gera_ip import bd_gera_ip
from sql_comandos.bd_select_login import bd_select_login


# RECEBENDO O COOKIE
print 'Content-Type: text/html\n'
cookie = Cookie.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
cookie_string = cookie_string.split(' ')[0].replace(';','')
valid_cookie = bd_select_login("select cookie from login where cookie='%s'" %cookie_string)
# VALIDANDO O COOKIE
if (cookie_string != valid_cookie) or (cookie_string[0] != "1"):
	print  "<script>self.location.href='manual.py';</script>"

# RECEBENDO SELECT DO BANCO E PRINTANDO NO HTML
if bd_select('c_caminho_conf','admconf') == '6':
	s_c_caminho_conf_c1 = 'CHECKED'
	s_c_caminho_conf_c2 = ''
else:
	s_c_caminho_conf_c1 = ''
	s_c_caminho_conf_c2 = 'CHECKED'

if bd_select('c_dns_update','admconf') == 'nao':
	s_c_dns_update_c1 = 'CHECKED'
	s_c_dns_update_c2 = ''
else:
	s_c_dns_update_c1 = ''
	s_c_dns_update_c2 = 'CHECKED'

if bd_select('c_autoritario','admconf') == 'nao':
	s_c_autoritario_c1 = 'CHECKED'
	s_c_autoritario_c2 = ''
else:
	s_c_autoritario_c1 = ''
	s_c_autoritario_c2 = 'CHECKED'
	
if bd_select('c_bootp','admconf') == 'nao':
	s_c_bootp_c1 = 'CHECKED'
	s_c_bootp_c2 = ''
else:
	s_c_bootp_c1 = ''
	s_c_bootp_c2 = 'CHECKED'
		
if bd_select('c_booting','admconf') == 'nao':
	s_c_booting_c1 = 'CHECKED'
	s_c_booting_c2 = ''
else:
	s_c_booting_c1 = ''
	s_c_booting_c2 = 'CHECKED'

# FORM STORAGE
form = cgi.FieldStorage() 
# BT ENVIAR DADOS CADASTRO NO HTML 
try:
	if form.getvalue('enviar'):	
		bd_gera_ip(form.getvalue('subnet'),form.getvalue('subnet_mask'))
		valores=bd_select_admconf().split(',')
		del valores[0]
		del valores[-1]
		for i in valores:
			bd_replace("admconf",i,form.getvalue(i[2:]))
			retorno = "<script>self.location.href='admconf.py';</script>"

except Exception, e:
	log_erro = "Error"			
		
print """
<html>
<head>
<title>Administra&ccedil;&atilde;o</title>

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
<legend>Dhcpd.conf</legend>
<table align="center" style="border: none;">
		<tr>
			<td align="center"><b>Local do Conf</b>
			</td>
		</tr>
</table>
<table align="center" style="border: none;">
		<tr>
			<td align="center">
				<input type="radio" name="caminho_conf" value="6" %s>/etc/dhcp/dhcpd.conf""" %s_c_caminho_conf_c1
print """		
		</td>
			<td align="center">
	    		<input type="radio" name="caminho_conf" value="5" %s>/etc/dhcpd.conf""" %s_c_caminho_conf_c2
print """	
			</td>
		</tr>
</table>
<table align="center" style="border: none;">
	<tr>
		<td align="center">
			<br /><b>Configura&ccedil;&atilde;o</b>					
		</td>
	</tr>
</table>
<table align="center" style="border: none;">
    <tr>
    	<td>
    		Ativar sevi&ccedil;o de dns:
    	</td>
	    <td>
	    	N&atilde;o:<input type="radio" name="dns_update" value="nao" %s>""" %s_c_dns_update_c1
print """
	    	Sim:<input type="radio" name="dns_update" value="sim" %s>""" %s_c_dns_update_c2
print """    	
	    </td>
	    <td>Gateway:
		 </td>
		  <td> 
		  	<input type="text" size="15" maxlength="15" name="gateway" value=%s>""" %bd_select('c_gateway','admconf')
print """
		  </td>
    </tr>
    <tr>
    		<td>
    			Ativar servidor autoritario:
    		</td>
	    	<td>
	    		N&atilde;o:<input type="radio" name="autoritario" value="nao" %s>""" %s_c_autoritario_c1
print """	    		
	    		Sim:<input type="radio" name="autoritario" value="sim" %s>""" %s_c_autoritario_c2
print """	    		
	    	</td>
	    		<td>
	    			Time-offset:
		    	</td>
		    	<td> <input type="text" size="15" name="offset" value="%s">""" %bd_select('c_offset','admconf')
print """		    	
		    	</td>
		</tr>
		<tr>
		    	<td>
		    		Ativar consulta bootp:
    			</td>
	    		<td>
	    			N&atilde;o:<input type="radio" name="bootp" value="nao" %s> """ %s_c_bootp_c1
print """	    		
	    			Sim:<input type="radio" name="bootp" value="sim" %s> """ %s_c_bootp_c2
print """	    			
	    		</td>
		    	<td>
		    		Ntp-servers :
		    	</td>
		    	<td> 
		    		<input type="text" size="15" name="ntp" value="%s">""" %bd_select('c_ntp','admconf')
print """		    		
		    	</td>
    			</tr>
    	<tr>
	    		<td>
	    			Ativar consulta booting:
    			</td>
	    		<td>
	    			N&atilde;o:<input type="radio" name="booting" value="nao" %s>""" %s_c_booting_c1
print """	    			
	    			Sim:<input type="radio" name="booting" value="sim" %s>""" %s_c_booting_c2
print """	    			
	    		</td>
		</tr>
	   <tr>
	    		<td>
	    			Subnet Rede:
		    	</td>
		    	<td> 
		    		<input type="text" size="15" maxlength="15" name="subnet" value="%s">""" %bd_select('c_subnet','admconf')
print """		    		
		    	</td>
		</tr>
		<tr>
				<td>
					Subnet Mask:
		    	</td>
		  		<td> 
		  			<input type="text" size="15" maxlength="15" name="subnet_mask" value="%s" title="Min 255.255.255.252 Max 255.255.0.0">""" %bd_select('c_subnet_mask','admconf')
print """		  			
		    	</td>
	   </tr>
		<tr>
				<td>
					Proxy Wpa Url:
		    	</td>
		    	<td> 
		    		<input type="text" size="30" maxlength="60" name="proxy_url" value="%s">""" %bd_select('c_proxy_url','admconf')
print """		    		
		    	</td>
		    	<td>
		    		PXE Path:
		    	</td>
		    	<td> 
		    		<input type="text" size="15" maxlength="30" name="pxe_path" value="%s">""" %bd_select('c_pxe_path','admconf')
print """		    		
		    	</td>	
    	</tr>
    	<tr>
		    	<td>
		    		Domain-name:
		    	</td>
		    	<td>
		    		<input type="text" size=30 maxlength="60" name="domain_name" value="%s">""" %bd_select('c_domain_name','admconf')
print """		    		
		    	</td>	
		    	<td>
		    		PXE filename:
		    	</td>
		    	<td>
		    		<input type="text" size="15" maxlength="30" name="pxe_filename" value="%s">""" %bd_select('c_pxe_filename','admconf')
print """		    		
		    	</td>
	 	</tr>
	  	<tr>
		   	<td>
		   		Domain-name-servers:
		   	</td>
		    	<td> 
		    		<input type="text" size="30" maxlength="60" name="name_servers" value="%s">""" %bd_select('c_name_servers','admconf')
print """		    		
		    	</td>
		    	<td>
		    		PXE next-server: 
		    	</td>
		    	<td>
		    		<input type="text" size="15"  maxlength="15" name="pxe_server" value="%s">""" %bd_select('c_pxe_server','admconf')
print """		    		
		    	</td>		
		</tr>
	  	<tr>
		    	<td>
		    		Netbios-name-servers :
		    	</td>
		    	<td> 
		    		<input type="text" size="30" maxlength="60" name="netbios_name" value="%s">""" %bd_select('c_netbios_name','admconf')
print """		    		
		    	</td>
		</tr>
		<tr>
		    <td>
		    	Default-lease-time:
		    </td>
		    <td>
		    	<input type="text" size="15" maxlength="15" name="deft_lease_time" value="%s">""" %bd_select('c_deft_lease_time','admconf')
print """		    	
		    </td>
		    <td>
		    	Max-lease-time:
		    </td>
		 	<td>
		 			<input type="text" size="15" maxlength="15" name="max_lease_time" value="%s">""" %bd_select('c_max_lease_time','admconf')
print """		 			
		    </td>
		</tr>
	   <tr>
	   	<td>
	    			Range Inicio:
	    	</td>
	    	<td>
	    			<input type="text" size="15" name="range_inicio" value="%s">""" %bd_select('c_range_inicio','admconf')
print """	   
			</td>
		</tr>
		<tr>
			<td> 			
		    		Range Fim:
		   </td>
		   <td>
		   		<input type="text" size="15" name="range_fim" value="%s">""" %bd_select('c_range_fim','admconf')
print """		    		
			</td>
		</tr>
	</table>
	<table align="center">
		<tr>
			<td>
				OBS: Campos em Branco(None) n&atilde;o ser&atilde;o ativados na inicializa&ccedil;&atilde;o do conf.
			</td>
		</tr>
		<tr>
		 	<td align="center">
		    		<input class="btn" type="submit" name="enviar" value="Cadastrar" onclick="return confirm('voc&ecirc; confirma?')"/> 
		    	</td>
		</tr>
	</table>
</fieldset>		
</form>
</body>
</head>
</html>
"""

print retorno

