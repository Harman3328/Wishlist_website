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


def share():
    fs = cgi.FieldStorage()
    if 'sharewith' in fs:
        shareid = fs['sharewith'].value
        shareid = ObjectId(shareid)
        person = db.A4Users.find_one({'_id':shareid})
        if person:
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
                    us = db.A4Users.find_one({'Username':user, "usid":usid})
                    usproducts = us['products']
                    shared = db.A4Users.find_one({'_id':shareid,'shared':{'$exists':True}})
                    o = ObjectId()
                    thisdict = {"From":us['Username'], "wishlist":usproducts, "id":o}
                    if shared:
                        db.A4Users.update_one({'Username':person['Username']},{'$push':{'shared':thisdict}})
                        print person['Username']
                    else:
                        db.A4Users.update_one({'Username':person['Username']},{'$set':{'shared':[thisdict]}})
                        print person['Username']


print "Content-Type: text/html"
print

share()