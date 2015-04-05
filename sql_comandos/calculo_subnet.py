#!/usr/bin/python
#-=- encoding: utf-8 -=-
def calcula_subnet(rede,mascara):
        # VARIAVEIS
        rede_input = rede
        mascara_input = mascara
        # cortando os campos pelo (.)
        classe = rede_input.split('.')
        mascara = mascara_input.split('.')
        
        # FUNCAO SUBTRACAO WILCARD
        def rede(receba):
            return 255 - receba
    
        # WILCARD
        a = rede(int(mascara[0]))
        b = rede(int(mascara[1]))
        c = rede(int(mascara[2]))
        d = rede(int(mascara[3]))
        wilcard=[a,b,c,d]
        
        # MASCARA DE REDE
        a = 255 #if (a == 0) else 255 - a
        b = 255 #if (b == 0) else 255 - b
        c = 255 
        if (c == 0):
            c = 255
        else:
            255 - c
         
        if (d == 0):
            d = 255
        else:
            255 - d
        
        # VALIDANDO A MASCARA DE REDE
        lista=(0,128,192,224,240,248,252,254,255)
        valida = 0
        for a in lista:
            for b in mascara:
                if a == int(b):
                    valida += 1
        if valida < 4:
            return "Subnet invalid"
                
        # PEGANDO O ULTIMO IP
        ip_a = int(classe[0]) #if int(lista1[0]) == 0 else int(classe[0]) + int(lista1[0])
        ip_b = int(classe[1]) #if int(lista1[1]) == 0 else int(classe[1]) + int(lista1[1])
        
        if int(wilcard[2]) > 1:
            ip_c = wilcard[2]
        else:
            if int(wilcard[2]) == 0 or int(wilcard[2]) > 1:
                ip_c = int(classe[2]) 
            else:
       		ip_c = int(classe[2]) + int(wilcard[2])
        
        if int(wilcard[3]) == 0:
            ip_d = int(classe[3]) 
        else:
      		ip_d = int(classe[3]) + int(wilcard[3])
        
        # GERANDO A RESPOSTA
        resposta  = "%s.%s.%s.%s\n" %(wilcard[0],wilcard[1],wilcard[2],wilcard[3])
        if int(wilcard[2]) > 0:
            resposta += "%s.%s.%s.%s\n" %(classe[0],classe[1],(wilcard[2]-wilcard[2]),int(classe[3])+1)
        else:
       		resposta += "%s.%s.%s.%s\n" %(classe[0],classe[1],classe[2],int(classe[3])+1)
        resposta += "%s.%s.%s.%s\n" %(ip_a,ip_b,ip_c,ip_d -1)
        
        cont = int(classe[3])
        while cont <= int(ip_d):
            cont2 = int(classe[2])
            cont += 1
            while cont2 <= int(ip_c):
                resposta += "%s.%s.%s.%s\n" %(classe[0],classe[1],cont2,cont -1)
                cont2 += 1
     
        return resposta

#print calcula_subnet('172.168.6.0','255.255.255.254')
