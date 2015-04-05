#!/usr/bin/python
#-=- encoding: latin-1 -=-

import MySQLdb
import re
from bd_variaveis import bd_variaveis
from bd_select import bd_select


# Recebendo as variaveis de acesso no banco
host        = 	bd_variaveis()[0]
user        = 	bd_variaveis()[1]
password    = 	bd_variaveis()[2]
bd_name     = 	bd_variaveis()[3]

def bd_replace(tabela,coluna,valor2):
    valor1 = bd_select(coluna,tabela)
    select =''
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    resultado = cursor.fetchone()
    sql = ("update admconf set %s= replace (%s, '%s', '%s') order by id desc limit 1" %(coluna,coluna,valor1,valor2))
    cursor.execute(sql)
    db.commit()
    cursor.close()
    
