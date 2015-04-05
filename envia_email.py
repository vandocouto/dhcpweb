#!/usr/bin/python

# LIBS
import os
import commands
import time
import smtplib
from email.MIMEText import MIMEText
from bd_select_smtp import bd_select_smtp

# FUNCAO ENVIA EMAIL
def envia_email(recebe1,recebe2):
    # DEFINA AS VARIAVEIS ABAIXO DE ACORDO COM O SEU AMBIENTE
    SMTP    =   bd_select_smtp("select smtpserver from smtp")
    PORTA   =   bd_select_smtp("select smtpporta from smtp")
    LOGIN   =   bd_select_smtp("select smtplogin from smtp")
    EMAIL   =   bd_select_smtp("select smtpemail from smtp")
    PASS    =   bd_select_smtp("select smtpsenha from smtp")
    if (PORTA == 465):
        SMTPSERVER = smtplib.SMTP_SSL
        PORTA = str(PORTA)
        ASSUNTO="DhcpWeb 2.0"
	HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s \nSenha: %s" %(HOSTNAME,recebe2)
        FROM=EMAIL
        TO=recebe1
        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.login(LOGIN,PASS)
        msg1 = MIMEText(MENSAGEM)
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
    else:
        SMTPSERVER = smtplib.SMTP
        PORTA = str(PORTA)
        ASSUNTO="DhcpWeb 2.0"
	HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s \nSenha: %s" %(HOSTNAME,recebe2)
        FROM=EMAIL
        TO=recebe1
        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.starttls()
        serv.login(LOGIN,PASS)
        msg1 = MIMEText(MENSAGEM)
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
  
