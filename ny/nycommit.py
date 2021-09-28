import os 
from sys import argv
import json 



baseJson  = "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"
def commitObj(baseJson):
    with open(baseJson, "r") as ppp:
        g = ppp.read()
        data = json.loads(g)

    for i in data["project"]:
        if i["name"] == argv[1]:
            return i["path"]
path = commitObj(baseJson)
with open(path + "/build/version.json", "r") as read_file:
        data = json.load(read_file)
        vers = data["version"]
        name = data["projName"]

os.system("git add dev/*")
os.system('git commit -m \"version: ' + vers + '"')
print("Version: " +  str(vers))
print("Date: "  + str(data["dataLastBuild"]))
