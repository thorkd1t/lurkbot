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
    #global bots
    #print bots
    for i in joinlist.joinlist:

        #do something different to check activity


        
        tempy = i + "/stillhere"
        tempy2 = i + "/yes"
        if not os.path.exists(tempy):
            
            print i + "'s bot... he ded...  Restarting :)"
            if os.path.exists(i):
                shutil.rmtree(i)
            thepath = os.path.abspath("gogogo.py")
            cmmd = 'python ' + 'gogogo.py ' + i
   
            Popen(cmmd, creationflags=CREATE_NEW_CONSOLE)
            

            
        
        if os.path.exists(tempy):
            if os.path.exists(tempy2):
                tempy = i + "/wait"
                os.makedirs(tempy)
                time.sleep(0.5)
                shutil.rmtree(tempy2)
                
            
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





checks = Timer(100, alivecheck)
checks.start()
