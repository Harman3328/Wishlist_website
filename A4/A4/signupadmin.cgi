#!/usr/bin/python
#Harmandeep Mangat || 6021109 || hm15mx
from pymongo import MongoClient
import cgi
import os
import hashlib
username = 'hm15mx'
password = '6021109'
client = MongoClient('mongodb://'+username+':'+password+'@127.0.0.1/'+username)
db = client[username]


def createNewUser():
    fs = cgi.FieldStorage()
    un = fs.getfirst('Uname')
    pw = fs.getfirst('Upass')
    gw = fs.getfirst('Gpass')

    if un!= None and pw != None and gw != None:
        auth = db.A4Users.find_one({'Username':'creator'},{'General':True,'_id':False})
        key2 = hashlib.md5(gw.encode())
        key2 = key2.hexdigest()
        if db.A4Users.find_one({"Username":un}) == None and auth['General'] == key2:
            key = hashlib.md5(pw.encode())
            key = key.hexdigest()
            record = {"Username":un, "Password":key, "Admin":"Y", "products":[]}
            rec_id1 = db.A4Users.insert_one(record)
            print "Location: ./login.cgi"
            return ''
        elif db.A4Users.find_one({"Username":un}) != None:
            return "Username already Exists"
        elif auth['General'] != key2:
            return "You don't have the correct permission"
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


accountType = createNewUser()
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
    "<p class='msg'>%s</p>"%(accountType)+\
    "<form action='#' method='post' autocomplete='off'>"+\
    "<input type='text' name='Uname' id='uname' placeholder='Username'/></br>"+\
    "<input type='text' name='Upass' id='pword' placeholder='Password'/></br>"+\
    "<input type='text' name='Gpass' id='pword' placeholder=' Admin Password'/></br>"+\
    "<input type='submit' class='submit2' name='signup' value='Sign Up'/>"+\
    "</form>"+\
    "</div>"
print open('bottom.html','r').read()
print "</body></html>"