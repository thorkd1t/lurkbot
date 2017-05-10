
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

re.purge() # some housekeeping
server = "irc.chat.twitch.tv"
port = 443

channohash = joinlist.joinlist[0] #set current channel to first in joinlist


channel = "#" + channohash


conn = sqlite3.connect('chatlog_db.db')
c = conn.cursor()

import os.path

counting = 1
def joinnxt(irc):
    global channohash
    
    global counting
    for i in joinlist.joinlist:
        if counting > len(joinlist.joinlist):
            counting = 1
            
        if i != channohash and counting == 1:         #           
            print i                                     #            
                                                          #             
            continue

        if counting > 1:
            tempy = i + "/bot1"
            if os.path.exists(tempy):
                os.removedirs(tempy)
                time.sleep(1)
                
            if not os.path.exists(i):
                
                os.makedirs(tempy)
                
                irc.send("PART " + "#" + channohash + "\r\n")
                channohash = i
                irc.send("JOIN " + "#" + i + "\r\n")
                print "bot 1 joining " + i
                counting = 1
                break
            else:
                print "next"
                continue
            
        
        if i == channohash:                     # if item is same as current saved channel            
                     
            if os.path.exists(i):               # if streamer folder exist
                tempy = i + "/bot1"
                if not os.path.exists(tempy):       # if it is in use by another bot
                    print "ohsheet"                 # move to next
                    counting += 1
                    continue
                else:
                    os.removedirs(tempy)   # if its not another bot it must be this ones so remove
                    
                    print "removed" + tempy
              # if counting > len(joinlist.joinlist):
               #     counting = 1
                #    break
                    counting += 1
                    continue # move to next item
            else:
                print "something happened"
                
                            
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
    tmp = channohash + "/bot1"
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
    tr = Timer(20.0, checker, [irC])
    tr.start()

ctimr = Timer (10.0, checker, [irc])
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
                 
                c.execute('select count (*) from clog1')
                temp = c.fetchone()
                #print temp[0]
                temp = temp[0] + 1
                c.execute('insert into clog1 values (?,?,?,?,?)',
                 (user, message, temp, flags, date))
                conn.commit()
                   
          
    

    except Exception as (e):
        date = time.strftime("%Y-%m-%dT%H:%M:%S")
        c.execute('select count (*) from clog1')
        temp = c.fetchone()
        #print temp[0]
        temp = temp[0] + 1
        conn.text_factory = 'utf-8'
        c.execute('insert into clog1 values (?,?,?,?,?)',
                 (user, message, temp, flags, date))
    
        conn.commit()
         
  
        conn.text_factory = 'string'

                    
    time.sleep(0.1)
   
    ############################



