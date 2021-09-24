#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi, os
import cgitb
from templates import login_page, secret_page, after_login_incorrect
from secret import password, username

try:
    from cgi import escape  # v3.7
except:
    from html import escape  # v3.8

def login():
    cgitb.enable()
    form = cgi.FieldStorage()

    in_username = form.getvalue('username')
    in_password = form.getvalue('password')
    if in_username is None and in_password is None:
        print(login_page())
    else:
        if in_password == password and in_username == username:
            print("Set-Cookie:Username =", username)
            print("Set-Cookie:Password =", password)
            print("Content-type:text/html\r\n\r\n")
        else:
            print(after_login_incorrect())
            return
        if "HTTP_COOKIE" in os.environ.keys():
            print(secret_page(username, password))
            co_password, co_username = None, None
            param = os.environ['HTTP_COOKIE'].strip()
            # for cookie in param.split('; '):
            #     try:
            #         (key, value) = cookie.split('=')
            #         if key == "Username":
            #             co_username = value
            #         if key == "Password":
            #             co_password = value
            #     except:
            #         pass



if __name__ == '__main__':
    login()





