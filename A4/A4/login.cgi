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


def userName():
    fs = cgi.FieldStorage()
    un = fs.getfirst('Uname')
    pw = fs.getfirst('Upass')

    if un != None and pw != None:
        key = hashlib.md5(pw.encode())
        key = key.hexdigest()
        if db.A4Users.find_one({"Username":un, "Password":key, "Ban":"N"}) != None:
            sid = uuid.uuid1().hex
            db.A4Users.update_one({"Username":un},{'$set':{'usid':sid}})
            print "Set-Cookie: user="+un
            print "Set-Cookie: usid="+sid
            print "Location: ./home.cgi"
            print 
            exit()
        elif db.A4Users.find_one({"Username":un, "Password":key, "Admin":"Y"}) != None:
            sid = uuid.uuid1().hex
            db.A4Users.update_one({"Username":un},{'$set':{'usid':sid}})
            print "Set-Cookie: user="+un
            print "Set-Cookie: usid="+sid
            print "Location: ./home.cgi"
            print 
            exit()
        elif db.A4Users.find_one({"Username":un, "Password":key}) == None:
            return "Incorrect Password, try again"
        else:
            return "You are Banned!"
    else:
        return "Enter Username and Password"

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


name = userName()
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
    "<body>"+\
    open('top.html','r').read()+\
    "<div class='form'>"+\
    "<p class='msg'>%s</p>"%(name)+\
    "<form action='#' method='post' autocomplete='off'>"+\
    "<input type='text' name='Uname' id='uname' placeholder='Username'/></br>"+\
    "<input type='text' name='Upass' id='pword' placeholder='Password'/></br>"+\
    "<input type='submit' class='submit2' value='Login'/>"+\
    "</form>"
print "<a href='signup.cgi' class='Slink'>Sign Up</a>"
print "</div>"
print open('bottom.html','r').read()
print "</body></html>"
