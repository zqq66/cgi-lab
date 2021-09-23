#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
from templates import secret_page
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

print(secret_page(username, password))