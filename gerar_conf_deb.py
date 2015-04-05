#!/usr/bin/python
#-=- encoding: latin-1 -=-

from bd_deb_dhip import bd_deb_dhip
from bd_select import bd_select

arquivo = ''

def gerar_conf_deb(recebe1,recebe2,recebe3):
    	arquivo = '# CONF DEBIAN - SOMENTE EDITAR NA INTERFACE  WEB - DHCPWEB\n%s' %recebe1
    
    # FUNÇÕES
	if(bd_select('c_dns_update','admconf') == "nao"):
		arquivo += ''
	else:
           	arquivo += "ddns-update-style interim\n%s" %recebe1
                    
	if(bd_select('c_autoritario','admconf') == "nao"):
		arquivo += ''
     	else:
		arquivo += "authoritative\n%s" %recebe1
                
	if(bd_select('c_bootp','admconf') == "nao"):
		arquivos += ''
      	else:
		arquivo += "allow bootp\n%s" %recebe1
                
	if(bd_select('c_booting','admconf') == "nao"):
		arquivo += ''
      	else:
		arquivo += "allow booting\n%s" %recebe1            
    # PXE
	if(bd_select('c_pxe_server','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "siaddr %s\n%s" %(bd_select('c_pxe_server','admconf'),recebe1)
                
	if(bd_select('c_pxe_filename','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "boot_file %s\n%s" %(bd_select('c_pxe_filename','admconf'),recebe1)
                
	if(bd_select('c_pxe_path','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "option rootpath %s\n%s" %(bd_select('c_pxe_path','admconf'),recebe1)

    # OPTION
	if(bd_select('c_name_servers','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "option dns %s\n%s" %(bd_select('c_name_servers','admconf'),recebe1)
                
	if(bd_select('c_subnet_mask','admconf') == "None"):
		arquivo += ''
	else:
		arquivo += "option subnet %s\n%s" %(bd_select('c_subnet_mask','admconf'),recebe1)
                
	if(bd_select('c_gateway','admconf') == "None"):
		arquivo += ''
    	else:
		arquivo += "option router %s\n%s" %(bd_select('c_gateway','admconf'),recebe1)
                
	if(bd_select('c_netbios_name','admconf') == "None"):
		arquivo += ''
     	else:
		arquivo +=  "option wins %s\n%s" %(bd_select('c_netbios_name','admconf'),recebe1)

	if(bd_select('c_domain_name','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "option domain %s\n%s" %(bd_select('c_domain_name','admconf'),recebe1)

	if(bd_select('c_ntp','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo += "option ntpsrv %s\n%s" %(bd_select('c_ntp','admconf'),recebe1)
                
	if(bd_select('c_proxy_url','admconf') == "None"):
		arquivo += ''
       	else:
		arquivo +=  "option wpad %s\n%s" %(bd_select('c_proxy_url','admconf'),recebe1)

	if(bd_select('c_max_lease_time','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "option lease %s\n%s" %(bd_select('c_max_lease_time','admconf'),recebe1)

    # RANGE IP
	if(bd_select('c_range_inicio','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "start %s\n%s" %(bd_select('c_range_inicio','admconf'),recebe1)

	if(bd_select('c_range_fim','admconf') == "None"):
		arquivo += ''
      	else:
		arquivo +=  "end %s\n%s" %(bd_select('c_range_fim','admconf'),recebe1)
                

    	arquivo += "#STATIC\n%s" %recebe1
    	arquivo += bd_deb_dhip(recebe2,recebe3) + '\n' 

    	return arquivo
