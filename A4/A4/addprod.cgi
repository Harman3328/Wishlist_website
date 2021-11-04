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


def addprod():
    fs = cgi.FieldStorage()
    prodname = fs.getfirst('Pname')
    prodcost = fs.getfirst('pcost')
    proddesc = fs.getfirst('pdesc')
    prodtag = fs.getfirst('ptag')
    prodimg = fs.getfirst('pimg')


    if prodname != None and prodcost != None and proddesc != None and prodtag != None and prodimg != None:
        prodtag = prodtag.split(",")
        prodimg = "Products/"+prodimg+".jpg"
        db.A4Products.insert_one({'name':prodname, 'cost':prodcost, 'desc':proddesc, 'pic':prodimg, 'tag':prodtag})
        print "Location: ./addprod.cgi?productname="+prodname
        print
        exit()
    else:
        return "Fill in all fields"

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

name = addprod()
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
    open('top3.html','r').read()+\
    "<div class='form'>"+\
    "<p class='msg'>%s</p>"%(name)+\
    "<form action='#' method='post' autocomplete='on'>"+\
    "<input type='text' name='Pname' id='pname' placeholder='Product Name'/></br>"+\
    "<input type='text' name='pcost' id='pcost' placeholder='Cost (Do not enter $)'/></br>"+\
    "<input type='text' name='pdesc' id='pdesc' placeholder='Description'/></br>"+\
    "<input type='text' name='ptag' id='ptag' placeholder='Tags (separate multiple entires with a comma)'/></br>"+\
    "<input type='text' name='pimg' id='pimg' placeholder='Picture Name'/></br>"+\
    "<input type='submit' class='submit2' value='Submit'/>"+\
    "</form>"
print "</div>"
print open('bottom.html','r').read()
print "</body></html>"
