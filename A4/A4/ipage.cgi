#!/usr/bin/python
#Harmandeep Mangat || 6021109 || hm15mx
from pymongo import MongoClient
from bson.objectid import ObjectId
import cgi
import os
import hashlib
import uuid
username = 'hm15mx'
password = '6021109'
client = MongoClient('mongodb://'+username+':'+password+'@127.0.0.1/'+username)
db = client[username]

def create():
    fs = cgi.FieldStorage()
    if 'product' in fs:
        prodid = fs['product'].value
        prodid = ObjectId(prodid)
        item = db.A4Products.find_one({'_id':prodid})
        print "<div class='product-body'>"
        print "<img src='"+item['pic']+"' class='responsive2'>"
        print "<h3>"+item['name']+" $"+item['cost']+"</h3>"
        print "<p>"+item['desc']+"</p></br>"
        print "<p>"
        for tag in item['tag']:
            print "Tag: "+tag+"</br>"
        print "</p>"
        return item
    else:
        return None

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
print "<link rel='stylesheet' media='screen' href='https://fontlibrary.org/face/semyon-soviet' type='text/css'/>"
if logedIn:
    if checkAdmin(logedIn):
        print "<script src='code3.js'></script>"
        print "<body>"
        print open('top3.html','r').read()
    else:
        print "<script src='code3.js'></script>"
        print "<body>"
        print open('top2.html','r').read()
else:
    print "<script src='code.js'></script>"
    print "<body>"
    print open('top.html','r').read()
item = create()
if item:
    print "<table>"
    print "<tr><th><button class='button' id='add."+str(item['_id'])+"' onclick='add();'>Add to Wishlist</button></th>"
    print "<th><button class='button' id='remove."+str(item['_id'])+"' onclick='remove();'>Remove</button></th></tr>"
    print "</table>"
    print "</div>"
print open('bottom.html','r').read()
print "</body></html>"
