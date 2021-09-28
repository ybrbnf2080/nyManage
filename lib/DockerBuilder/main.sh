#!/bin/bash

cd /src/

echo startBuild  $@

wine python -m pip install -U -r ./requirements.txt
if [ $# -eq 0 ]
    then
        wine pyinstaller --onefile --clean ./dev/main.py
        echo "No arguments supplied"
else 
    wine pyinstaller --onefile --clean ./dev/$1
        
fi
exit
