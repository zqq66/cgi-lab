#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os, json
import cgi
import cgitb
cgitb.enable()

print("Content-type:text/html\r\n\r\n")

print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

# print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)

# Q2
for param in os.environ.keys():
    if param == "QUERY_STRING":
        print("<b>%20s</b>: %s<b>" % (param, os.environ[param]))

# Q3

for param in os.environ.keys():
    if param == "HTTP_USER_AGENT":
        print("<b>%20s<b>: %s<br>" % (param, os.environ[param]))

# Q5

for param in os.environ.keys():
    if param == "HTTP_COOKIE":
        print("<b>%20s<b>: %s<br>" % (param, os.environ[param]))
