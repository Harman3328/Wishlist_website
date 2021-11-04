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

print "Content-Type: text/html"
print

fs = cgi.FieldStorage()
if 'product' in fs:
    prodid = fs['product'].value
    prodid = ObjectId(prodid)
    print db.A4Products.find_one({'_id':prodid})['name']
else:
    print "nope"

