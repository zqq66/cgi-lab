#!/usr/bin/python
import os

print("Set-Cookie:UserID = XYZ;\r\n")
print("Set-Cookie:Password = XYZ123;\r\n")
print("Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT;\r\n")
print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
print("Set-Cookie:Path = /perl;\n")
print("Content-type:text/html\r\n\r\n")

for param in os.environ.keys():
    if param == "HTTP_COOKIE":
        print("<b>%20s<b>: %s<br>" % (param, os.environ[param]))

