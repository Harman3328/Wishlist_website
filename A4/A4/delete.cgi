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


def dele():
    fs = cgi.FieldStorage()
    if 'product' in fs:
        prodid = fs['product'].value
        prodid = ObjectId(prodid)
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
                person = db.A4Users.find_one({'Username':user, "usid":usid})
                if person['Admin'] == "Y":
                    removed = db.A4Products.find_one({'_id':prodid})
                    db.A4Products.remove({'_id':prodid})
                    allUsers = db.A4Users.find()
                    for singleuser in allUsers:
                        items = singleuser['products']
                        name = singleuser['Username']
                        for i in items:
                            if removed['_id'] in i.values():
                                db.A4Users.update_one({'Username':singleuser['Username']},{'$pull':{'products':{'id':removed['_id']}}})
                                break


dele()

print "Content-Type: text/html"
print