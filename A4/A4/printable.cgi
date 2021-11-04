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

def create(user):
    print "<table class='product listing' id='mytable'>"
    print "<thead><tr><td><h3>Name</h3></td><td><h3>Cost</h3></td></tr></thead>"
    items = db.A4Users.find_one({'Username':user})['products']
    for item in items:
        prodid = item['id']
        print "<tr><td>"+item['name']+"</td><td>$"+item['cost']+"</td></tr>"
    print "</table>"

def changetheme():
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
if logedIn == None:
    print "Location: ./login.cgi"

changeto = changetheme()

print "Content-Type: text/html"
print

print "<html>"+\
    "<meta charset='utf-8'>"+\
    "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+\
    "<title>Home</title>"+\
    "<meta name='viewport' content='width=device-width, initial-scale=1'>"
if changeto:
    if changeto == 'Normal':
        print "<link rel='stylesheet' href='style.css'>"
    elif changeto == 'Purple':
        print "<link rel='stylesheet' href='style2.css'>"
else:
    print "<link rel='stylesheet' href='style.css'>"
print "<link rel='stylesheet' media='screen' href='https://fontlibrary.org/face/semyon-soviet' type='text/css'/>"+\
    "<body>"
if checkAdmin(logedIn):
    print open('top3.html','r').read()
else:
    print open('top2.html','r').read()
print "<div id='wrapper'>"
create(logedIn)
print "</div>"
print open('bottom.html','r').read()
print "</body></html>"
