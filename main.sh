# !/bin/bash

echo NYhelper welcom \n 
case $1 in 
    h | help)
        echo "s | start"
        echo "b | build"
        echo "in | init"
        echo "up | update"
        echo "vi | view"
        ;;
    s | start)
        echo start new project
        python ~/.local/bin/nylinuxUtil/ny/nys.py --name=$2 --env=$3 --desk=$4 --path=$5
        ;;
    b | build)
        echo start build project
        python ~/.local/bin/nylinuxUtil/ny/nyb.py $2
        ;;
    in | init)
        echo "initialisations for project"
        python ~/.local/bin/nylinuxUtil/ny/nyinit.py $2 $3 $4 
        ;;
    up | update)
        echo start update list proj
        python ~/.local/bin/nylinuxUtil/ny/nyup.py $@
        ;;
    vi | view)
        echo list your project
        python ~/.local/bin/nylinuxUtil/ny/nyview.py $@
        ;;
    com | commit)
        echo git commit your project
        python ~/.local/bin/nylinuxUtil/ny/nycommit.py $2
        ;;
esac