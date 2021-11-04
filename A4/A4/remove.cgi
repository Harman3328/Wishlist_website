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


def remov():
    fs = cgi.FieldStorage()
    if 'product' in fs:
        prodid = fs['product'].value
        prodid = ObjectId(prodid)
        item = db.A4Products.find_one({'_id':prodid})
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
                items = person['products']
                for i in items:
                    if item['_id'] in i.values():
                        db.A4Users.update_one({'Username':user},{'$pull':{'products':{'id':item['_id']}}})
                        break


remov()

print "Content-Type: text/html"
print