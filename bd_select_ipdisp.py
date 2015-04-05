#!/usr/bin/python
#-=- encoding: latin-1 -=-

import MySQLdb
import re
from bd_variaveis import bd_variaveis

# Recebendo as variaveis de acesso no banco
host        = 	bd_variaveis()[0]
user        = 	bd_variaveis()[1]
password    = 	bd_variaveis()[2]
bd_name     = 	bd_variaveis()[3]

# função insert 
def bd_select_ipdisp():
    resultado=''
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    sql = ()
    cursor.execute("select rede.ip_address from rede where rede.ip_address not in (select ip_address from dhcp) order by inet_aton (ip_address)")
    select = cursor.fetchone()
    while (select):
        resultado += "<option value='%s'>%s</option>\n" %(select[0],select[0])
        select = cursor.fetchone()
    cursor.close()
    return resultado