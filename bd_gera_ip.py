#!/usr/bin/python
#-=- encoding: utf-8 -=-

import MySQLdb
import re
from bd_variaveis import bd_variaveis
from calculo_subnet import calcula_subnet

# Recebendo as variaveis de acesso no banco
host        = 	bd_variaveis()[0]
user        = 	bd_variaveis()[1]
password    = 	bd_variaveis()[2]
bd_name     = 	bd_variaveis()[3]


def bd_gera_ip(rede,mask):
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    cursor.execute("delete from rede")
    db.commit()
    classe_mascara = calcula_subnet(rede,mask)
    wicard = classe_mascara.split('\n')[0]
    primeiro_ip = classe_mascara.split('\n')[1]
    ultimo_ip = classe_mascara.split('\n')[2]
    ips = wicard,primeiro_ip,ultimo_ip  
    for i in classe_mascara.split('\n')[4:-2]:
        cursor.execute("insert into rede (ip_address) values ('%s')" %i)
    db.commit()
    cursor.close()

