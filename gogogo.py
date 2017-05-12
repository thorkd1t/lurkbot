import lurkbotclass
import joinlist
import sys

bots = {}

thename = sys.argv[1]

def gobots(name):
    
    global bots
    bots[name] = lurkbotclass.LurkBot(name)
    bots[name].ircJoin(name)

gobots(thename)
