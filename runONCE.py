import sqlite3
import time

conn = sqlite3.connect('chatlog_db.db')
c = conn.cursor()



   

try:
    c.execute('select * from clog1')
    print " clog1 already exists..."
except Exception:
    print 'hi, adding table clog1..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog1 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog1 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################

try:
    c.execute('select * from clog2')
    print " clog2 already exists..."
except Exception:
    print 'hi, adding table clog2..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog2 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog2 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()

##################################################

try:
    c.execute('select * from clog3')
    print " clog3 already exists..."
except Exception:
    print 'hi, adding table clog3..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog3 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog3 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()

####################################################

try:
    c.execute('select * from clog4')
    print " clog4 already exists..."
except Exception:
    print 'hi, adding table clog4..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog4 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog4 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()

##########################################################

try:
    c.execute('select * from clog5')
    print " clog5 already exists..."
except Exception:
    print 'hi, adding table clog5..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog5 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog5 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################

try:
    c.execute('select * from clog6')
    print " clog6 already exists..."
except Exception:
    print 'hi, adding table clog6..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog6 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog6 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################
try:
    c.execute('select * from clog7')
    print " clog7 already exists..."
except Exception:
    print 'hi, adding table clog7..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog7 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog7 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################
try:
    c.execute('select * from clog8')
    print " clog8 already exists..."
except Exception:
    print 'hi, adding table clog8..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog8 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog8 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################
try:
    c.execute('select * from clog9')
    print " clog9 already exists..."
except Exception:
    print 'hi, adding table clog9..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog9 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog9 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################
try:
    c.execute('select * from clog10')
    print " clog10 already exists..."
except Exception:
    print 'hi, adding table clog10..'
    date = time.strftime('%d/%m/%Y')
    firststart = """ create table if not exists clog10 (
                        usr text,
                        mesg text,
                        id integer primary key,
                        flags text,
                        date_time text
                        
            );"""

c.execute(firststart)
date = time.strftime("%Y-%m-%dT%H:%M:%S")
print date
c.execute('insert into clog10 values (?,?,?,?,?)',
              (":Ref:", "hello world", 1, "bla", date))
conn.commit()
##############################################

conn.close()
print 'sucessful'
