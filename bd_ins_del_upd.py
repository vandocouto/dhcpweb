#!/usr/bin/python
#-=- encoding: latin-1 -=-

import MySQLdb
from bd_variaveis import bd_variaveis

# Recebendo as variaveis de acesso no banco
host        = 	bd_variaveis()[0]
user        = 	bd_variaveis()[1]
password    = 	bd_variaveis()[2]
bd_name     = 	bd_variaveis()[3]

# função update
def bd_ins_del_upd(recebe):
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    sql = (recebe)
    cursor.execute(sql)
    db.commit()
    cursor.close()
