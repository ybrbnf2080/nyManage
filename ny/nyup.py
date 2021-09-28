from datetime import date
import os 
from nys import editJson
import json
baseJson  = "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"
def popit(date):
    t = 0
    for i in date["project"]:
        if os.path.exists(i["path"]) != True :
            date["project"].pop(t)
                
        t +=1 
with open(baseJson, "r") as ppp:
    g = ppp.read()
    base = json.loads(g)

json.dump(base, open(baseJson, "w"), indent=4)
