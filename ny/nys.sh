# !/bin/bash 

pwd 

if [ -n "$2" ]
then
    mkdir $2
else
    mkdir ./$1
fi

pref= /usr/bin/ny/nylinuxUtil/lib/pref
cp $pref/* ./$1

cd $1

rm -r build/pref build/main dev/__pycache__
rm building/* file/* main.spec dist/* 

python /home/ybrbnf/ny/nylinuxUtil/ny/nys.py

mkdir build/$1
