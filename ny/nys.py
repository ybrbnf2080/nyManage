from datetime import datetime
import os
import json
import argparse
from shutil import copyfile, copytree, rmtree
from types import DynamicClassAttribute
from typing_extensions import TypeAlias
patPref = "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/lib/pref"
pathBaseJson= "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"




parser = argparse.ArgumentParser(description='A tutorial of argparse!')
la = os.getcwd()
print(la)
parser.add_argument("--dir", default=la, type=str, help="dir for create proj ")
parser.add_argument("--env", default=False, type=bool, help="create virtualenv?")
parser.add_argument("--desk", default=None, type=str, help="descriptions")
args = parser.parse_args()

pat = args.dir +"/"+ os.argv[1]

def preparationFold():  # copy pref to folder new proj, and preparetion proj 
        
    try:                                   
        copytree(patPref, args.dir +"/"+ os.argv[1]+"/" )
    except FileExistsError:
        os.system("rm -r "+ pat)
        copytree(patPref, args.dir +"/"+ os.argv[1]+"/" )
    rmtree(pat + "/build/pref")
    rmtree(pat + "/build/main")
    rmtree(pat + "/dev/__pycache__")

    os.system("cd " + args.dir +"/"+ os.argv[1] + " && rm building/* file/* main.spec dist/* ")
    os.mkdir(pat +"/" +"build/" + os.argv[1])
    if args.env == True:
        os.system("cd " + args.dir +"/"+ os.argv[1] + " && python -m venv .env")

def editingJsonBase():
        
    with open(pathBaseJson, "r") as ppp:

        g = ppp.read()
        base = json.loads(g)
        print(base)
    base["project"].append({
        "name": os.argv[1],
        "dateStart": str(datetime.now()),
        "path" : pat,
        "descriptions": args.desk,

    })
    print(base)
    json.dump(base, open(pathBaseJson, "w"), indent=4)

    with open(pat + "/build/version.json", "r") as read_file:
            data = json.loads(read_file.read())
            data.update({
                "projName": os.argv[1],
                "version": 0.0,
                "author": base["author"],
                "dateCreateProj": str(datetime.now()),
                "descriptions": args.desk,
                "fileFold": "file",
                "dataLastBuild": "none"
            })
            
            json.dump(data, open(pat + "/build/version.json", "w"), indent=4)



if __name__ =="__main__":
    preparationFold()

    editingJsonBase()