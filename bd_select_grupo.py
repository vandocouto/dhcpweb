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

# fun��o insert 
def bd_select_grupo(coluna,tabela,ordenacao):
    resultado=''
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    sql = ("select id,%s from %s %s" %(coluna,tabela,ordenacao))
    cursor.execute(sql)
    select = cursor.fetchone()
    while (select):
        resultado += "<option value='%s'>%s</option>\n" %(select[1],select[1])
        select = cursor.fetchone()
    cursor.close()
    return resultado.lower()


