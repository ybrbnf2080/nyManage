import json
import os 
from sys import argv

pathBaseJson= "~/.local/nylinuxUtil/base.json"
pathBuildBash= "~/.local/nylinuxUtil/ny/build.sh"
name = argv[1]
print(name)
fil = open(pathBaseJson, "r")

js = json.loads(fil.read())
for i in  js["project"] :
    if i["name"] == name:
        pat = i["path"]
        print(pat)

os.system("cd "+ pat + " && " + pathBuildBash) 











