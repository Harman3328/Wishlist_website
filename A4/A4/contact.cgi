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

def create():
    print "<div class='contact-body'>"+\
        "<ul>"+\
            "<li>https://www.google.com/url?sa=i&url=https%3A%2F%2Ffr.123rf.com%2Fphoto_88064083_concept-de-magasinage-en-ligne-avec-des-ic%25C3%25B4nes-d-achat-et-de-livraison-banni%25C3%25A8re-pour-site-web-ou-magaz.html&psig=AOvVaw2JXy8O6axvZsHFQUkDdONO&ust=1601779688796000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMCyqti0l-wCFQAAAAAdAAAAABAD</li>"+\
            "<li>https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.theverge.com%2Fcircuitbreaker%2F2019%2F12%2F13%2F21020149%2Fxbox-series-x-pc-specs-analysis&psig=AOvVaw1iCseSQqxmx2diVyk423rO&ust=1602211397173000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjo5Nz8o-wCFQAAAAAdAAAAABAD</li>"+\
            "<li>https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.radiotimes.com%2Ftechnology%2F2020-09-30%2Fps5-release-date%2F&psig=AOvVaw0DpXIlIwtQB0LiI-gsmAW0&ust=1602256526079000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLDL24elpewCFQAAAAAdAAAAABAD</li>"+\
            "<li>https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.ca%2FAssassins-Creed-Valhalla-Xbox-One%2Fdp%2FB087ZLWCB1&psig=AOvVaw1QH0s1Wo_f-EM15z2JFf0X&ust=1602259124300000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjG7MmupewCFQAAAAAdAAAAABAD</li>"+\
            "<li>https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ign.com%2Farticles%2Fcyberpunk-2077-has-gone-gold&psig=AOvVaw2TkZKZQJZYhSooFdcOEWOd&ust=1602259351896000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLDopq-vpewCFQAAAAAdAAAAABAD</li>"+\
            "<li>https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.ca%2FDark-Souls-III-Fire-Fades%2Fdp%2FB06XTPJWWL&psig=AOvVaw2WgMwYVOps-aRJE3ZtA9ep&ust=1605491760754000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLjw3oO5g-0CFQAAAAAdAAAAABAD</li>"+\
            "<li>https://www.microsoft.com/en-ca/p/xbox-series-x/8wj714n3rbtl</li>"+\
            "<li>https://www.pocket-lint.com/games/news/playstation/143354-sony-playstation-5-release-date-rumours-and-everything-you-need-to-know-about-ps5</li>"+\
            "<li>https://www.ubisoft.com/en-ca/game/assassins-creed/valhalla</li>"+\
            "<li>https://store.steampowered.com/app/1091500/Cyberpunk_2077/</li>"+\
            "<li>https://fontlibrary.org/face/semyon-soviet</li>"+\
            "<li>https://www.cgmagonline.com/wp-content/uploads/2020/11/demons-souls-ps5-review-2.jpg</li>"+\
            "<li>https://store.playstation.com/en-ca/product/UP9000-PPSA01342_00-DEMONSSOULS00000</li>"+\
            "<li>https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/</li>"+\
            "<li>https://s2.gaming-cdn.com/images/products/943/orig/the-witcher-3-wild-hunt-xbox-one-cover.jpg</li>"+\
            "<li>https://images-na.ssl-images-amazon.com/images/I/719G5ws-qmL._AC_SL1500_.jpg</li>"+\
            "<li>https://images-na.ssl-images-amazon.com/images/I/61bF5-QAX%2BL._AC_SX385_.jpg</li>"+\
            "<li>https://images-na.ssl-images-amazon.com/images/I/71aMIzGEYTL._AC_SL1500_.jpg</li>"+\
            "<li>https://images-na.ssl-images-amazon.com/images/I/61m7vCH%2B2PL._SX425_.jpg</li>"+\
            "<li>https://images-na.ssl-images-amazon.com/images/I/81tgXrGI2YL._AC_SL1500_.jpg</li>"+\
            "<li>https://images-na.ssl-images-amazon.com/images/I/813xlI-NGpL._SL1500_.jpg</li>"+\
        "</ul>"+\
    "</div>"


logedIn = checkLogedIn()
changeto = changetheme()

print "Content-Type: text/html"
print


print "<html>"+\
    "<meta charset='utf-8'>"+\
    "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+\
    "<title>Contact</title>"+\
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
    print "<body>"
    if checkAdmin(logedIn):
        print open('top3.html','r').read()
    else:
        print open('top2.html','r').read()
else:
    print "<body>"+\
        open('top.html','r').read()

create()
print open('bottom.html','r').read()
print "</body></html>"
