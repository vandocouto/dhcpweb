#!/usr/bin/python
#-=- encoding: latin-1 -=-

# Importando os módulos 
import cgi, cgitb, Cookie, os, time, re


print 'Content-Type: text/html\n'
print """<html>
<head>
<title>DhcpWeb 2.0</title>
<body>
<br>
<style>
body {
	background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAIAAAACUFjqAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QsZDiQNvXI8RAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVBjTY/z//z8DbsDEgBcMXWmW////4pP+8+srAwPOkAEAxw8J+pT6JekAAAAASUVORK5CYII=);
	}
	
	.border {border-style:solid;}
	.copy, .copy a {width: 660px; margin:0 auto; color: #DD8888;}
	.formresult {background-color:#FFFF99;display:block;padding:10px;}
	.seletor {font-family: Arial, Sans-Serif; font-size:6px;} g:10px;}

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
<h2><center>DhcpWeb 2.0</center></h2>
<p align="justify">
O DhcpWeb &eacute; uma interface baseada em Html, Python e Mysql.<br />
Muito &uacute;til para realizar &agrave; administra&ccedil;&atilde;o do servi&ccedil;o de dhcp em sistema GNU/Linux CentOS 5/6 e Debian 7.</p>
O DhcpWeb elimina a necessidade de editar manualmente o arquivo de configura&ccedil;&atilde;o dhcp.conf ou udhcpd.conf.
Com ele &eacute; poss&iacute;vel Cadastrar, Bloquear e Consultar um Host fixo atrav&eacute;s do Mac Address.</p>
<a href="http://dhcpweb.tutoriaisgnulinux.com/">Download</a>
<br /><br /></p>
<h3>Cadastro de Grupo-IP e/ou Host</h3>
Nesta tela &eacute; poss&iacute;vel cadastrar e/ou remover um grupo e/ou mac address.<br />
<h3>Castrado de Host</h3>
Nesta tela &eacute; poss&iacute;vel fixar o mac address a um ip dispon&iacute;vel na lista.<br />
<h3>Dhcp.conf</h3>
Neta tela &eacute; poss&iacute;vel configurar o dhcpd.conf de acordo com o par&acirc;metros oferecidos em cada campo.<br />
<h3>Hosts Ativos</h3>
Nesta tela &eacute; poss&iacute;vel listar cada em orderm alfabetica: Hostname, Ip Address, Mac Addres e Grupo-IP.<br />
<h3>Remover Host</h3>
Nesta tela &eacute; poss&iacute;vel remover um Host pelo mac address e/ou bloquer um determinado ip na tabela arp.<br />
OBS: &Eacute; importante que o servidor tenha o pacote arping2 instalado.<br />
<h3>Pacotes necess&aacute;rios</h3>
<p>Debian 7<p>
<pre>
<font color="#FC0824"># apt-get install udhcpd arping apache2 mysql-server python-mysqldb sudo</font>
</pre>
CentOS 5 e 6
<pre>
<font color="#FC0824"># yum install dhcp arp-scan  httpd mysql-server MySQL-python</pre></font>
<h3>Arquivo sudoers</h3>
No arquivo sudoers adicione a linha abaixo:<br /><br />
Debian 7
<pre>
<font color="#FC0824">www-data ALL=NOPASSWD: /usr/sbin/udhcpd, /etc/init.d/udhcpd, /bin/cp, /usr/sbin/arp<br /></font>
</pre>
CentOS 5 e 6
<pre>
<font color="#FC0824">Defaults requiretty<br />
para<br />
# Defaults requiretty<br /></font>
<font color="#FC0824">apache ALL=NOPASSWD: /usr/sbin/dhcpd, /etc/init.d/dhcpd, /bin/cp, /sbin/arp<br /></font>
</pre>
Debian 7 <br />
<pre>
<font color="#FC0824"># chown -R www-data.www-data dhcpweb/<br />
# chmod -R 755 dhcpweb/<br />
# mv dhcpweb /usr/lib/cgi-bin/</font>
</pre>
CentOS 5 e 6
<pre>
<font color="#FC0824"># chown -R apache.apache dhcpweb/<br />
# chmod -R 755 dhcpweb/<br />
# mv dhcpweb /var/www/cgi-bin/</font>
</pre>
<h3>Configurando o Banco de Dados - Mysql</h3>
<pre>
<font color="#FC0824"># mysql -u root -psenha -h localhost<br />
mysql> create database dhcpweb;<br />
# cd dhcpweb/dump/<br />
# mysql -u root -psenha dhcpweb < dhcpweb.sql<br /></font></pre>
<h3>Configurando as variáveis de acesso ao banco de dados Mysql</h3>
<pre>
<font color="#FC0824"># cd dhcpweb/sql_comandos/<br /></font>
</pre>
<pre>
<font color="#FC0824"># vim bd_variaveis.py<br /><br />
# Abaixo defina os campos do banco de dados<br />
    host = 'IP do Banco/Hostname'<br />
    user = 'user'<br />
    password = 'senha'<br />
    bd_name = 'dhcpweb'<br /></font>
</pre>
<h3>Arquivo /etc/default/udhcpd</h3>
<pre>
<font color="#FC0824"># vim /etc/default/udhcpd<br /> 
DHCPD_ENABLED="no"<br />
para <br />
DHCPD_ENABLED="yes"
</pre></font>
<h3>Acessando o sistema</h3>
<pre>
<font color="#FC0824">http://IP/cgi-bin/dhcpweb/inicio.py<br />
User: admin<br />
senha: admin<br /></font>
</pre>

<h4><center>Desenvolvido por</center></h4>
<center><a href="http://tutoriaisgnulinux.com/">TutoriaisGNU/Linux.com</a></center><br />
<center><i>LEMBRE DE DEUS EM TUDO O QUE FIZER, E ELE LHE MOSTRARÁ O CAMINHO CERTO"</i></center><br/ >
<center><i>Prov&eacute;rbios de Salom&atilde;o (3.6)</i></center>
</form>
</body>
</head>
</html>
"""
 
