from datetime import datetime
import os
import json
import argparse
from shutil import copyfile, copytree, rmtree
from sys import argv
from types import DynamicClassAttribute
from typing_extensions import TypeAlias
def editJson(base, name, pat, desk): 
    base["project"].append({
        "name": name,
        "dateStart": str(datetime.now()),
        "path" : pat,
        "descriptions": desk,

    })
    return base
def checkBase(path, name ):
    with open(path, "r") as ppp:
        g = ppp.read()
        base = json.loads(g)


        for i in base["project"]:
            if i["name"] == name:
                print("!!!a project with such a name already exists!!!")
                quit()
        
        ppp.close()

if __name__ =="__main__":
    patPref = "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/lib/pref"
    pathBaseJson= "/home/" + str(os.getlogin()) + "/.local/bin/nylinuxUtil/base.json"




    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    la = os.getcwd()
    print(la)
    try:
        parser.add_argument("--name", default="iloveyou", type=str, help="name for create proj ")
        parser.add_argument("--dir", default=la, type=str, help="dir for create proj ")
        parser.add_argument("--env", default=False, type=bool, help="create virtualenv?")
        parser.add_argument("--desk", default=None, type=str, help="descriptions")
        args = parser.parse_args()
    except: 
        print("Error pars arg")
        quit()
    pat = args.dir +"/"+ args.name
    checkBase(pathBaseJson,  args.name)

def preparationFold(name, path, env):  # copy pref to folder new proj, and preparetion proj 
        
    try:                                   
        copytree(patPref, path +"/"+ name+"/" )
    except FileExistsError:
        os.system("rm -r "+ pat)
        copytree(patPref, path +"/"+ name+"/" )
    rmtree(pat + "/build/pref")
    rmtree(pat + "/build/main")
    rmtree(pat + "/dev/__pycache__")

    os.system("cd " + path +"/"+ name + " && rm building/* file/* main.spec dist/* ")
    os.mkdir(pat +"/" +"build/" + name)
    if env == True:
        os.system("cd " + path +"/"+ name + " && python -m venv .env")

def editingJsonBase():
        
    with open(pathBaseJson, "r") as ppp:
        g = ppp.read()
        base = json.loads(g)
        #print(base)
    base =  editJson(base, args.name, pat, args.desk)
    print(base)
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



if __name__ =="__main__":
    preparationFold(args.name, args.dir, args.env)

    editingJsonBase()