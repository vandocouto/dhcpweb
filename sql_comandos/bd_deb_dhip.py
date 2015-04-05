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
def bd_deb_dhip(recebe1,recebe2):
    resultado=''
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    cursor.execute(recebe1)
    select = cursor.fetchone()
    while (select):
        resultado += "static_lease %s %s\n%s" %(select[0],select[1],recebe2)
        select = cursor.fetchone()
    return resultado.lower()
    cursor.close()

