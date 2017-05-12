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
from subprocess import Popen, CREATE_NEW_CONSOLE
import shutil
from itertools import count




class LurkBot(object):
    _ids = count(0)
   
    CREATE_NEW_CONSOLE = (0x00000010)
    def __init__(self, name):
        print "hi"
        self.name = name
        self.id = self._ids.next()

    def iamstillhere():
        joinlist.counts[self.name] += 1
        im = Timer(30, iamstillhere)
        im.start()
        
    def tablecheck(self, name):
        tempy = name + ".db"
        connx = sqlite3.connect(tempy)
        cu = connx.cursor()
        
        try:
            
            blah = "select * from chat"
            cu.execute(blah)
         
            connx.close()
            print "table exists already, skipping"
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
                        channel text,
                        date_time text
                        
                );"""
            
            
            print "firststart ran"
            time.sleep(2)
            cu.execute(firststart)
            date = time.strftime("%Y-%m-%dT%H:%M:%S")
            print date
            strings = "insert into chat"  
            cu.execute(strings + " values (?,?,?,?,?,?)",
              ("username", "message", 1, "flags", "channel", date))
            connx.commit()
            connx.close()

    def stillAlive(self, name):
        
        self.name = name
        tempy = str(name) + "/wait"
        if os.path.exists(tempy):
            time.sleep(0.5)
        tempy = str(name) + "/stillhere"
        if not os.path.exists(tempy):
            os.makedirs(tempy)
        al = Timer(120, self.stillAlive, [str(name)])
        al.start()
    

    def ircJoin(self, channohash = joinlist.joinlist[0]):
        im = Timer(30, iamstillhere)
        im.start()
        os.system("title " + channohash)
        print channohash
        self.name = channohash
        lalala = Timer(8, self.stillAlive, [channohash])
        lalala.start()
        
        if not self.tablecheck(channohash):
            print "creating table for channel :  " + channohash
        re.purge() # housekeeping?
        server = "irc.chat.twitch.tv"
        port = 443
        tempy = channohash + ".db"
        conn = sqlite3.connect(tempy)
        c = conn.cursor()                    
        # init socket
        startplz = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connect to said socket
        startplz.connect((server, port))
        # wrap in ssl
        irc = ssl.wrap_socket(startplz)

        ##################################
        # login  #
        # irc.send("PASS " + botcfg.oa + '\r\n')
        irc.send("NICK " + "justinfan420" + '\r\n')
        # capabilities request
        irc.send("CAP REQ :twitch.tv/membership" + "\r\n")
        # and join channel

        if not os.path.exists(channohash):
            os.mkdir(channohash)
            irc.send("JOIN " + "#" + channohash + '\r\n')
            print "joining " + channohash
    
        else:
            print "folder exists, is another bot active in this channel?"
            time.sleep(20)
            quit()
        
        
        ##############################################################
        irc.send("CAP REQ :twitch.tv/tags" + "\r\n")
        ########"@"@"@"@"@"@"@"@"@"@""@"@

        CHAT_MSG=re.compile(r"@.+?PRIVMSG.+?(:){1}") # New (for irc flags mode)


        messagetemp = ""
        messagcount = 0
        print str(self.id) + " class instances running.."
        while True:
            
            if self.id > len(joinlist.joinlist):
                print "something went wrong...."
                time.sleep(1)
            if self.id > len(joinlist.joinlist) + 5:
                print "something went really wrong...."
                time.sleep(100)

            #gets output from IRC server
            #data = irc.recv(1204)
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

            
            if (messagetemp) == (message) and (message) == "" or (message) == None:
                messagcount += 1
                if messagcount > 10:
                    print "dropped connection, to " + channohash + " reconnecting..."
                    
                    thepath = os.path.abspath("gogogo.py")
                    cmmd = 'python ' + 'gogogo.py ' + channohash
                    if os.path.exists(channohash):
                        shutil.rmtree(channohash)
                    messagcount = 0
                    Popen(cmmd, creationflags=CREATE_NEW_CONSOLE)
            
            messagetemp = message
 
            print (user + ": " + message) # new (for flags mode)

            try:
                unicode(message[0:5], "utf-8")
                if "tmi.twitch.tv" not in (user) and "tmi.twitch.tv" not in (message) and (user) != "":
                    if "jtv MODE" not in (user) and "justinfan" not in (user) and (user) != "twitchnotify":
                        date = time.strftime("%Y-%m-%dT%H:%M:%S")

                        blah = "select count (*) from chat"
                        c.execute(blah)
                        temp = c.fetchone()
                        #print temp[0]
                        temp = temp[0] + 1
                        blah = "insert into chat"
                    
                        c.execute(blah + " values (?,?,?,?,?,?)",
                                  (user, message, temp, flags, channohash, date))
                        conn.commit()
                   
            except Exception as (e):
                if (user) != "":
                    date = time.strftime("%Y-%m-%dT%H:%M:%S")
                    blah = "select count (*) from chat"
                    c.execute(blah)
                    temp = c.fetchone()
                    #print temp[0]
                    temp = temp[0] + 1
                    conn.text_factory = 'utf-8'

                    blah = "insert into chat"
                    c.execute(blah + " values (?,?,?,?,?,?)",
                                  (user, message, temp, flags, channohash, date))    
                    conn.commit()
           
                    conn.text_factory = 'string'

                    
            time.sleep(0.1)
   
        ############################

if __name__ == "__main__":
    print "__main__ is running"
    if os.path.exists(joinlist.joinlist[0]):
        shutil.rmtree(joinlist.joinlist[0])
    x = LurkBot(joinlist.joinlist[0])
    x.ircJoin(joinlist.joinlist[0])

    
