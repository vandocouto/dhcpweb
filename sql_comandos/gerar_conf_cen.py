#!/usr/bin/python
#-=- encoding: latin-1 -=-

from bd_deb_dhip import bd_deb_dhip
from bd_cen_dhip import bd_cen_dhip
from bd_select import bd_select

arquivo = ''

def gerar_conf_cen(recebe1,recebe2,recebe3):
  	arquivo = '# CONF CENTOS - SOMENTE EDITAR NA INTERFACE  WEB - DHCPWEB\n%s' %recebe1
    
    # FUNÇÕES
	if(bd_select('c_dns_update','admconf') == "nao"):
		arquivo += ''
      	else:
		arquivo += "ddns-update-style interim;\n%s" %recebe1
                    
	if(bd_select('c_autoritario','admconf') == "nao"):
		arquivo += ''
       	else:
		arquivo +=  "authoritative;\n%s" %recebe1
                
	if(bd_select('c_bootp','admconf') == "nao"):
		arquivo += ''
     	else:
		arquivo +=  "allow bootp;\n%s" %recebe1
                
	if(bd_select('c_booting','admconf') == "nao"):
		arquivo += ''
      	else: 
		arquivo += "allow booting;\n%s" %recebe1 
    
    	arquivo += """\noption wpad-url code 252 = text;\n\
%soption option-128 code 128 = string;\n\
%soption option-129 code 129 = text;%s\n\n""" %(recebe1,recebe1,recebe1)

    	recebe1

	if(bd_select('c_subnet','admconf') == "None"):
		arquivo += ''
	else: 
		arquivo += "subnet %s " %(bd_select('c_subnet','admconf'))
	
	if(bd_select('c_subnet_mask','admconf') == "None"):
		arquivo += ''
     	else:
		arquivo +=  "netmask %s {\n%s" %(bd_select('c_subnet_mask','admconf'),recebe1)                
    
	if(bd_select('c_gateway','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "option routers %s;\n%s" %(bd_select('c_gateway','admconf'),recebe1)
    
	if(bd_select('c_subnet_mask','admconf') == "None"):
		arquivo += ''
    	else:
		arquivo +=  "option subnet-mask %s;\n%s" %(bd_select('c_subnet_mask','admconf'),recebe1)
                    
	if(bd_select('c_domain_name','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  'option nis-domain "%s";\n%s' %(bd_select('c_domain_name','admconf'),recebe1) 
    
	if(bd_select('c_domain_name','admconf') == "None"):
		arquivo += ''
     	else:
		arquivo +=  'option domain-name "%s";\n%s' %(bd_select('c_domain_name','admconf'),recebe1)  
                    
	if(bd_select('c_name_servers','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  'option domain-name-servers %s;\n%s' %(bd_select('c_name_servers','admconf'),recebe1) 
                    
	if(bd_select('c_netbios_name','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  'option netbios-name-servers %s;\n%s' %(bd_select('c_netbios_name','admconf'),recebe1)
    
	if(bd_select('c_offset','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo += 'option time-offset %s\n%s' %(bd_select('c_offset','admconf'),recebe1)                 
                    
	if(bd_select('c_ntp','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  'option ntp-servers %s;\n%s' %(bd_select('c_ntp','admconf'),recebe1)               
                    
	if(bd_select('c_proxy_url','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo += 'option wpad-url "%s";\n%s' %(bd_select('c_proxy_url','admconf'),recebe1)                
                    
	if(bd_select('c_pxe_path','admconf') == "None"):
		arquivo += ''
    	else:
		arquivo += 'option root-path "%s";\n%s' %(bd_select('c_pxe_path','admconf'),recebe1) 
    
	if(bd_select('c_pxe_server','admconf') == "None"):
		arquivo += ''
     	else:
		arquivo +=  'next-server %s;\n%s' %(bd_select('c_pxe_server','admconf'),recebe1)
                    
	if(bd_select('c_pxe_filename','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  'filename "%s";\n%s' %(bd_select('c_pxe_filename','admconf'),recebe1)
    
	if(bd_select('c_range_inicio','admconf') == "None"):
		arquivo += ''
       	else:
		arquivo +=  'range dynamic-bootp %s' %(bd_select('c_range_inicio','admconf'))
    
	if(bd_select('c_range_fim','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  ' %s;\n%s' %(bd_select('c_range_fim','admconf'),recebe1)
    
	if(bd_select('c_deft_lease_time','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  'default-lease-time %s;\n%s' %(bd_select('c_deft_lease_time','admconf'),recebe1)
                    
	if(bd_select('c_max_lease_time','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo += 'max-lease-time %s;\n}\n%s' %(bd_select('c_max_lease_time','admconf'),recebe1)                    
    
    	arquivo += "#STATIC\n%s" %recebe1
    	arquivo += bd_cen_dhip(recebe2,recebe3) + '\n'

    	return arquivo
