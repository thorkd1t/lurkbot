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
import os.path

class LurkBot(object):

    def __init__(self):
        self.name = "bob"
    
    def tablecheck(self, name):
        try:
            tempy = name + ".db"
            connx = sqlite3.connect(tempy)
            cu = connx.cursor()
            blah = "select * from " + name
            cu.execute(blah)
         
            connx.close()
            return True
        except Exception as (e):
            print e
            date = time.strftime('%d/%m/%Y')
            firsts = "create table if not exists chat"
            print name

            firststart = firsts
            
            firststart += """ (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
                );"""
            print firststart
            
            print "firststart ran"
            time.sleep(3)
            cu.execute(firststart)
            date = time.strftime("%Y-%m-%dT%H:%M:%S")
            print date
            strings = "insert into chat"  
            cu.execute(strings + " values (?,?,?,?,?)",
              (":Ref:", "hello world", 1, "bla", date))
            connx.commit()
            connx.close()

    def stillAlive(self):
        tempy = name + "/areyoustillthere"
        if os.path.exists(tempy):
            os.rename(tempy, "yes")
        al = Timer(120, stillAlive)
        al.start()
    

    def ircJoin(self, channohash = joinlist.joinlist[0]):
        if not self.tablecheck(channohash):
            print "creating table for channel :  " + channohash
        re.purge() # housekeeping?
        server = "irc.chat.twitch.tv"
        port = 443
        tempy = channohash + ".db"
        conn = sqlite3.connect(tempy)
        c = conn.cursor()                    
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
            os.makedirs(channohash)
            irc.send("JOIN " + "#" + channohash + '\r\n')
            print "joining " + channohash
    
        else:
            print "folder exists, is another bot active in this channel?"
            time.sleep(20)
            quit()
        stillAlive()
        
        ##############################################################
        irc.send("CAP REQ :twitch.tv/tags" + "\r\n")
        ########"@"@"@"@"@"@"@"@"@"@""@"@

        CHAT_MSG=re.compile(r"@.+?PRIVMSG.+?(:){1}") # New (for irc flags mode)

        while True:

            #gets output from IRC server
            data = irc.recv(1204)
            try:
                data = irc.recv(1204)
            except Exception as e:
                print e


            # ping/pong
            if data == "PING :tmi.twitch.tv\r\n":
                irc.send("PONG :tmi.twitch.tv\r\n")
              

            user = data.split('!', 1)[-1]
  
            user = user.split('@')[0]
    
            message = CHAT_MSG.sub("", data)
            flags = data.split(':', 1)[0]
 
            print (user + ": " + message) # new (for flags mode)

            if user == None:
                print "user == none"
            if user == "":
                print "user == quotes"

            try:
                unicode(message[0:5], "utf-8")
                if "tmi.twitch.tv" not in (user) and "tmi.twitch.tv" not in (message) and (user) != "":
                    if "jtv MODE" not in (user) and "justinfan" not in (user) and user != "twitchnotify":
                        date = time.strftime("%Y-%m-%dT%H:%M:%S")

                        blah = "select count (*) from " + channohash
                        c.execute(blah)
                        temp = c.fetchone()
                        #print temp[0]
                        temp = temp[0] + 1
                        blah = "insert into chat"
                    
                        c.execute(blah + " values (?,?,?,?,?)",
                                  (user, message, temp, flags, date))
                        conn.commit()
                   
          
    

            except Exception as (e):
                if (user) != "":
                    date = time.strftime("%Y-%m-%dT%H:%M:%S")
                    blah = "select count (*) from " + channohash
                    c.execute(blah)
                    temp = c.fetchone()
                    #print temp[0]
                    temp = temp[0] + 1
                    conn.text_factory = 'utf-8'

                    blah = "insert into chat"
                    c.execute(blah + " values (?,?,?,?,?)",
                                  (user, message, temp, flags, date))    
                    conn.commit()
           
                    conn.text_factory = 'string'

                    
            time.sleep(0.1)
   
        ############################

b = LurkBot()

b.ircJoin()
