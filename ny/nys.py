from datetime import datetime
import os
import json
import argparse
from shutil import copyfile, copytree, rmtree
from types import DynamicClassAttribute
from typing_extensions import TypeAlias
patPref = "~/.local/nylinuxUtil/lib/pref"
pathBaseJson= "~/.local/nylinuxUtil/base.json"




parser = argparse.ArgumentParser(description='A tutorial of argparse!')
la = os.getcwd()
parser.add_argument("--dir", default=la, type=str, help="dir for create proj ")
parser.add_argument("--name", required=True, type=str, help="name proj")
parser.add_argument("--desk", default=None, type=str, help="descriptions")
args = parser.parse_args()

pat = args.dir +"/"+ args.name
try: 
        
    copytree(patPref, args.dir +"/"+ args.name+"/" )
except FileExistsError:
    os.system("rm -r "+ pat)
    copytree(patPref, args.dir +"/"+ args.name+"/" )
rmtree(pat + "/build/pref")
rmtree(pat + "/build/main")
rmtree(pat + "/dev/__pycache__")

os.system("cd " + args.dir +"/"+ args.name + " && rm building/* file/* main.spec dist/* ")
os.mkdir(pat +"/" +"build/" + args.name)
os.system("cd " + args.dir +"/"+ args.name + " && python -m venv .env")
with open(pathBaseJson, "r") as ppp:

    g = ppp.read()
    base = json.loads(g)
    print(base)
base["project"].append({
    "name": args.name,
    "dateStart": str(datetime.now()),
    "path" : pat,
    "descriptions": args.desk,

})

json.dump(base, open(pathBaseJson, "w"), indent=4)

with open(pat + "/build/version.json", "r") as read_file:
        data = json.loads(read_file.read())
        data.update({
            "projName": args.name,
            "version": 0.0,
            "author": base["author"],
            "dateCreateProj": str(datetime.now()),
            "descriptions": args.desk,
            "fileFold": "file",
            "dataLastBuild": "none"
        })
        
        json.dump(data, open(pat + "/build/version.json", "w"), indent=4)
    