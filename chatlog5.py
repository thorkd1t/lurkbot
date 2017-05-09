# -*- coding: utf_8 -*-
import socket
import ssl
import time
import re
import random
from threading import *
import sqlite3
import string
import joinlist
counter = 0
re.purge() # some housekeeping
server = "irc.chat.twitch.tv"
port = 443
channohash = "thor10768765"  # target channel without the hashkey
channel = "#" + channohash
#currentchan = channohash
joincount = 0
conn = sqlite3.connect('chatlog_db.db')
c = conn.cursor()

import os.path




counting = 1
def joinnxt(irc):
    global channohash
    #global joinlist
    global counting
    for i in joinlist.joinlist:
        if counting > len(joinlist.joinlist):
            counting = 2
            break
        
        if i != channohash and counting == 1:
            print i
            continue

        if counting > 1:
            if not os.path.exists(i):
                tempy = i + "/bot5" 
                os.makedirs(tempy)
                channohash = i
                irc.send("JOIN " + "#" + i + "\r\n")
                counting = 2
                break
            else:
                continue
                    
        if i == channohash:                    
            # if it is kill the folder          
            if os.path.exists(i):
                if not os.path.exists(i + "/bot5"):
                    print "ohsheet"
                    counting += 1
                    continue
                tempy = i + "/bot5"
                os.removedirs(tempy)
                
                print "removed"
                if counting > len(joinlist.joinlist):
                    counting = 2
                    break
                counting += 1
                continue # move to next item
                            
# init socket
self = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect to said socket
self.connect((server, port))
# wrap in ssl
irc = ssl.wrap_socket(self)

##################################
# login  #
# irc.send("PASS " + botcfg.oa + '\r\n')
irc.send("NICK " + "justinfan420" + '\r\n')
# capabilities request
irc.send("CAP REQ :twitch.tv/membership" + "\r\n")
# and join channel


if not os.path.exists(channohash):
    tmp = channohash + "/bot5"
    os.makedirs(tmp)
    irc.send("JOIN " + channel + '\r\n')
    
else:
    joinnxt(irc)
    
##############################################################
irc.send("CAP REQ :twitch.tv/tags" + "\r\n")
########"@"@"@"@"@"@"@"@"@"@""@"@

CHAT_MSG=re.compile(r"@.+?PRIVMSG.+?(:){1}") # New (for irc flags mode)


datatemp = ""


dtemp = ""
def checker(irC):
    global dtemp
    
    if dtemp == data:
        print "sames"
        
        joinnxt(irC)
    dtemp = data
    tr = Timer(10.0, checker, [irC])
    tr.start()

ctimr = Timer (5.0, checker, [irc])
ctimr.start()

while True:
    

        #gets output from IRC server
    
    data = irc.recv(1204)
    try:
        data = irc.recv(1204)
    except Exception as e:
        print e
    
    
    datatemp = data 

   # ping/pong
    if data == "PING :tmi.twitch.tv\r\n":
        irc.send("PONG :tmi.twitch.tv\r\n")
              

    user = data.split('!', 1)[-1]
  
    user = user.split('@')[0]
    
    message = CHAT_MSG.sub("", data)
    flags = data.split(':', 1)[0]
 
    print (user + ": " + message) # new (for flags mode)


    try:
        unicode(message[0:5], "utf-8")
        if "tmi.twitch.tv" not in (user) and "tmi.twitch.tv" not in (message):
            if "jtv MODE" not in (user) and "justinfan" not in (user) and user != "twitchnotify":
                date = time.strftime("%Y-%m-%dT%H:%M:%S")
                  #  c.execute('select * from clog5')
                c.execute('select count (*) from clog5')
                temp = c.fetchone()
                #print temp[0]
                temp = temp[0] + 1
                c.execute('insert into clog5 values (?,?,?,?,?)',
                 (user, message, temp, flags, date))
                conn.commit()
          
    

    except Exception as (e):
        date = time.strftime("%Y-%m-%dT%H:%M:%S")
        c.execute('select count (*) from clog5')
        temp = c.fetchone()
        #print temp[0]
        temp = temp[0] + 1
        conn.text_factory = 'utf-8'
        c.execute('insert into clog5 values (?,?,?,?,?)',
                 (user, message, temp, flags, date))
        conn.commit()
  
        conn.text_factory = 'string'

                    
    time.sleep(0.1)
   
    ############################



