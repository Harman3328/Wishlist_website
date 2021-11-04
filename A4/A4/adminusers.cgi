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
    if isAdmin != "Y":
        print "Location: ./home.cgi"

def allUsers():
    print "<table class='product listing' id='mytable'>"
    print "<thead><tr><td><h3>Username</h3></td><td><h3>Ban</h3></td></tr></thead>"
    nonAdminUsers = db.A4Users.find({'Admin':"N"})
    for nonAdmin in nonAdminUsers:
        uid = nonAdmin['_id']
        if nonAdmin['Ban'] == "N":
            print "<tr><td>"+nonAdmin['Username']+"</td><td><input type='button' value='Ban' id='ban."+str(uid)+"' onclick='ban()' class='button'</td></tr>"
        elif nonAdmin['Ban'] == "Y":
            print "<tr><td>"+nonAdmin['Username']+"</td><td><input type='button' value='Unban' id='Unban."+str(uid)+"' onclick='Unban()' class='button'</td></tr>"
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
else:
    checkAdmin(logedIn)

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
    "<script src='code6.js'></script>"+\
    "<body>"+\
    open('top3.html','r').read()+\
    "<div id='wrapper'>"
allUsers()
print "</div>"
print open('bottom.html','r').read()
print "</body></html>"
