#!/usr/bin/python
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

print "Content-Type: text/html"
print


person = db.A4Users.find_one({'Username':"creator"})
items = person['products']
for i in items:
    print i['id']
        

