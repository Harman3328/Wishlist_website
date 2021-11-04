#!/usr/bin/python
#Harmandeep Mangat || 6021109 || hm15mx
from pymongo import MongoClient
import cgi
import os
import hashlib
import uuid
username = 'hm15mx'
password = '6021109'
client = MongoClient('mongodb://'+username+':'+password+'@127.0.0.1/'+username)
db = client[username]


def checkLogedIn():
    if os.environ.has_key('HTTP_COOKIE'):
        user = None
        usid = None
        cookies = os.environ['HTTP_COOKIE'].split(';')
        for cookie in cookies:
            if cookie.split('=')[0].strip()=='user':
                user = cookie[cookie.find('=')+ 1:]
            elif cookie.split('=')[0].strip()=='usid':
                usid = cookie[cookie.find('=')+1:]
        if user and usid:
            rec = db.A4Users.find_one({'Username':user, "usid":usid})
            if rec != None:
                return user
    return None

def checkAdmin(user):
    person = db.A4Users.find_one({'Username':user})
    isAdmin = person['Admin']
    if isAdmin == "Y":
        return True
    else:
        return False

def changetheme():
    fs= cgi.FieldStorage()
    theme = fs.getfirst('theme')
    
    if theme != None:
        print "Set-Cookie: theme="+theme
        print "Location: ./theme.cgi"
        print 
        exit()

def themechange():
    if os.environ.has_key('HTTP_COOKIE'):
        theme = None
        cookies = os.environ['HTTP_COOKIE'].split(';')
        for cookie in cookies:
            if cookie.split('=')[0].strip()=='theme':
                theme = cookie[cookie.find('=')+ 1:]
        if theme:
            return theme
    return None


logedIn = checkLogedIn()
changetheme()
changeto = themechange()

print "Content-Type: text/html"
print

print "<html>"+\
    "<meta charset='utf-8'>"+\
    "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+\
    "<title>Theme</title>"+\
    "<meta name='viewport' content='width=device-width, initial-scale=1'>"
if changeto:
    if changeto == 'Normal':
        print "<link rel='stylesheet' href='style.css'>"
    elif changeto == 'Purple':
        print "<link rel='stylesheet' href='style2.css'>"
else:
    print "<link rel='stylesheet' href='style.css'>"
print "<link rel='stylesheet' media='screen' href='https://fontlibrary.org/face/semyon-soviet' type='text/css'/>"
print "<body>"
if logedIn:
    if checkAdmin(logedIn):
        print open('top3.html','r').read()
    else:
        print open('top2.html','r').read()
else:
    print open('top.html','r').read()
print "<p class='msg'>Select a theme</p></br></br>"
print "<div class='form'>"+\
    "<form action='#' method='post'>"+\
    "<input type='radio' name='theme' id='normal' value='Normal'/>"+\
    "<label for='normal'>Normal</label>"+\
    "<input type='radio' name='theme' id='purple' value='Purple'/>"+\
    "<label for='purple'>Purple</label></br>"+\
    "<input type='submit' class='submit2' value='Change'/>"+\
    "</form>"
print "</body></html>"
