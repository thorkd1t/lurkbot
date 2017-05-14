import sqlite3
import time
import joinlist

# the tables look like this:
# db name 'imaqtpie.db' (each channel in joinlist has its own .db)
# Table name chat (each db has one table named 'chat')
#___________________________________________________________________
#  usr  | mesg  | id  |   flags   | channel   |     date/time      |
#===================================================================
#  bob  |   hi  |  1  |  @badges= | imaqtpie  |2017-05-01 12:00:00 |
#-------------------------------------------------------------------
#  jim  | Kappa |  2  | @badges=  | imaqtpie  |2017-05-01 12:00:01 |
#-------------------------------------------------------------------


target = "imaqtpie" #channel name

conn = sqlite3.connect(target + '.db')
c = conn.cursor()

#====================================================================
#example queries:
#------------------
#c.execute('select usr from chat')
#c.execute('select * from chat')
#c.execute('select * from chat where usr == ""')
#c.execute('select mesg from chat where usr == "moobot" order by id desc limit 5')
c.execute('select * from chat order by id desc limit 50')
bla = c.fetchall()

if bla != None:
    for i in bla:
        print i[0] + ": " + i[1]
else:
    print "nothing to print"
conn.close()
time.sleep(100)

