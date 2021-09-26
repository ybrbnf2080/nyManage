import json
import os 
from sys import argv

pathBaseJson= "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"
pathBuildBash= "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/ny/build.sh"
name = argv[1]
fil = open(pathBaseJson, "r")
pat= 1
#print(fil.read())
js = json.loads(fil.read())
for i in  js["project"] :
    if i["name"] == name:
        pat = i["path"]
        print(pat)

os.system("cd "+ pat + " && " + pathBuildBash) 











