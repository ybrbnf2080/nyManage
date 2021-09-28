import os 
import json


baseJson  = "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"
with open(baseJson, "r") as ppp:
    g = ppp.read()
    base = json.loads(g)

print(base["author"])
for i in base["project"]:
    if i["descriptions"] == None:
        i["descriptions"]= "lol"
    print("name:  " + i["name"] + "       date start: " + i["dateStart"] +"\n   " +
    str(i["descriptions"])+ "      " +  i["path"])