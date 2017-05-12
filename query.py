import sqlite3
import time
import joinlist

target = "imaqtpie" #channel name
conn = sqlite3.connect(target + '.db')
c = conn.cursor()

#c.execute('select usr from chat')
#c.execute('select * from chat')
#c.execute('select * from chat where usr == ""')

c.execute('select mesg from chat where usr == "moobot" order by id desc limit 5')

bla = c.fetchall()

for i in bla:
    print i[0]
conn.close()
time.sleep(100)

