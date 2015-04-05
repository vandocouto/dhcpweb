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
def bd_list_ip(recebe):
    resultado=''
    HOST = host
    USER = user
    PASSWORD = password
    db = MySQLdb.connect(HOST, USER, PASSWORD)
    cursor = db.cursor()
    cursor.execute("use %s" %bd_name)
    cursor.execute(recebe)
    select = cursor.fetchone()
    while (select):
        resultado += "<tr> \
        <td bgcolor='#BEBEBE'><font size='2'>%s</font></td> \
        <td bgcolor='#DCDCDC'><font size='2'>%s</font></td> \
        <td bgcolor='#BEBEBE'><font size='2'>%s</font></td> \
        <td bgcolor='#DCDCDC'><font size='2'>%s</font></td> \
        <td bgcolor='#BEBEBE'><font size='2'>%s</font></td> \
        </tr>" \
        %(select[0],select[1],select[2],select[3],select[4])
        select = cursor.fetchone()
    return resultado.lower()
    cursor.close()
