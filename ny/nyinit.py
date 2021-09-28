import os 
import sys
import json
sys.path.insert(0, "~/.local/bin/nylinuxUtil/ny")
from nys import editJson, checkBase, preparationFold
from sys import argv, path
try : 
    name = argv[1]
    path = argv[2]
    desk = argv[3]
except IndexError: 
    if len(argv) <= 2:
        path = os.getcwd()
    desk = "lol error descriprions(("


os.system("cp -r ./ ../cashe")

preparationFold(name, path, True)

os.system("cp -R ../cashe ./dist")

baseJson  = "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"
checkBase(baseJson, name)
with open(baseJson, "r") as ppp:
    g = ppp.read()
    base = json.loads(g)
editJson(base, name, path, desk)
json.dump(base, open(baseJson, "w"), indent=4)
