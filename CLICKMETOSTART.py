import time
from threading import *
import joinlist
import os.path
import lurkbotclass
import os
from subprocess import Popen, CREATE_NEW_CONSOLE
import shutil

CREATE_NEW_CONSOLE = (0x00000010)


def alivecheck():
    
    for i in joinlist.joinlist:
        tempy = i + "/stillhere"
        if not os.path.exists(tempy):
            
            print "he ded"
            thepath = os.path.abspath("gogogo.py")
            cmmd = 'python ' + 'gogogo.py ' + i
   
            Popen(cmmd, creationflags=CREATE_NEW_CONSOLE)
            

            
        tempy2 = i + "/yes"
        if os.path.exists(tempy2):
            os.removedirs(tempy2)
        if os.path.exists(tempy):
            
            os.rename(tempy, tempy2)
    
    checks = Timer(300, alivecheck)
    checks.start()
    
for i in joinlist.joinlist:
    if os.path.exists(i):
        shutil.rmtree(i)

thepath = os.path.abspath("gogogo.py")    
for i in joinlist.joinlist:

    
    cmmd = 'python ' + 'gogogo.py ' + i
   
    Popen(cmmd, creationflags=CREATE_NEW_CONSOLE)





checks = Timer(10, alivecheck)
checks.start()
