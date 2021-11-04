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



def search():
    fs = cgi.FieldStorage()
    prod = fs.getfirst('search')

    if prod:
        return prod
    else:
        return None

def printAll():
    allProd = db.A4Products.find()
    for prod in allProd:
        print "<tr><td><a href='ipage.cgi?product="+str(prod['_id'])+"'><img src='"+prod['pic']+"'><a/></td><td>"+"<a class='product-link' href='ipage.cgi?product="+str(prod['_id'])+"'>"+prod['name']+"</td><td><p class='cost'>$"+prod['cost']+"</p></td><td class='box'><button id='add."+str(prod['_id'])+"' onclick='add();'>Add</button>/<button id='remove."+str(prod['_id'])+"' onclick='remove();'>Remove</button></td></tr>"

def printSpecific(pName):
    allprod = db.A4Products.find({'tag':{'$regex':'^'+pName}})
    for prod in allprod:
        print "<tr><td><a href='ipage.cgi?product="+str(prod['_id'])+"'><img src='"+prod['pic']+"'><a/></td><td>"+"<a class='product-link' href=ipage.cgi?product="+str(prod['_id'])+"'>"+prod['name']+"</td><td><p class='cost'>$"+prod['cost']+"</p></td><td class='box'><button id='add."+str(prod['_id'])+"' onclick='add();'>Add</button>/<button id='remove."+str(prod['_id'])+"' onclick='remove();'>Remove</button></td></tr>"

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
prod = search()

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
    print "<script src='code3.js'></script>"
    print "<body>"
    if checkAdmin(logedIn):
        print open('top3.html','r').read()
    else:
        print open('top2.html','r').read()
else:
    print "<script src='code.js'></script>"
    print "<body>"+\
        open('top.html','r').read()

print "<div class='form'>"+\
    "<form action='#' method='post'>"+\
    "<input type='text' name='search' id='search' placeholder='Enter Tag'/>"+\
    "<input type='submit' class='submit' value='Search'/>"+\
    "</form>"
print "<table class='products-page'>"
if prod:
    printSpecific(prod)
else:
    printAll()  
print "</table>"
print open('bottom.html','r').read()
print "</div>"+\
    "</body></html>"
