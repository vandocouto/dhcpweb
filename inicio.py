#!/usr/bin/python
#-=- encoding: latin-1 -=-

#HTML
print 'Content-Type: text/html\n'
print """
<html>
<head><title>Dhpc Web 2.0</title></head>

        <frameset cols="320,*" scroll=no frameborder="NO" border="0" align="center">
        <frame src="menu.py" name=esqueda scrolling=no noresize id="esquerda">

        <frameset cols="1920,*" frameborder="NO" border="0" align="center">
        <frame src="manual.py" name="centro" id="centro">
        </frameset> 
        </frameset>

        <body>Dhcp Web 2.0</body>
        </noframes></body></html>
</head>
</html>
"""
