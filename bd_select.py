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
def bd_select(coluna,tabela):
    select =''
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    resultado = cursor.fetchone()
    sql = ("select %s from %s order by id desc limit 1" %(coluna,tabela))
    cursor.execute(sql)
    resultado = cursor.fetchone()
    while(resultado):
        select += str(resultado)
        resultado = cursor.fetchone()
    valor_id = str(select)
    new_str = re.sub('[()[L\]\']', '', valor_id)
    cursor.close()
    return new_str[0:-1]
