import sqlite3
import time

conn = sqlite3.connect('chatlog_db.db')
c = conn.cursor()

c.execute('select usr from clog1')
bla = c.fetchall()
print "users from t1"
print bla
c.execute('select usr from clog2')
bla = c.fetchall()
print "users from t2"
print bla
conn.close()
time.sleep(100)
