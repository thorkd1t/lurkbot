import os.path
import joinlist
import shutil




for i in joinlist.joinlist:
    if os.path.exists(i):
        shutil.rmtree(i)
