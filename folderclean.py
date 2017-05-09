import os.path
import joinlist
import shutil




for i in joinlist.joinlist:
    if os.path.exists(i):
        #tempy = i + "/"
        shutil.rmtree(i)
        #os.removedirs(tempy)
