import json
import os
import sys
import shutil
from datetime import datetime
from shutil import copyfile, copytree

with open("./build/version.json", "r") as read_file:
        data = json.load(read_file)
        vers = data["version"]
        name = data["projName"]

def collect(data):
    shutil.rmtree("./build/"+name)
    os.mkdir("./build/"+name)
    copyfile("./dist/main.exe", "./build/"+name+"/main.exe")
    copytree("./"+ data["fileFold"], "./build/" +name+ "/" + data["fileFold"])

def ziping(data, vers):
    #print(str(vers)[-1])
    if str(vers)[-1] == "9" :
        verse = str(int(str(vers)[2:]) + 2)
    else: 
    #    print(int(str(vers)[2:]) + 1)
        verse = str(int(str(vers)[2:]) + 1)
    vers = str(vers)[:2] + verse 
    data.update({
        "version": float(vers),
        "dataLastBuild": str(datetime.now())
    })
    with open("./build/version.json", "w") as read_file:
        
        json.dump(data, read_file, indent=4)
    
    copyfile("./build/version.json", "./build/"+name+"/version.json")

    
    shutil.make_archive("./building/"+name +"V"+ str(vers  ) , 'zip', "./build/"+name)
    return vers

if __name__ == "__main__":
    collect(data)
    print(data)
    vers = ziping(data, vers)
    
    print("version: " +  str(data["version"]))
    print("date: "  + str(data["dataLastBuild"]))
    os.system("git add dev/*")
    os.system('git commit -m \"version: ' + vers+ '"')
    print("Version: " +  str(data["version"]))
    print("Date: "  + str(data["dataLastBuild"]))



    