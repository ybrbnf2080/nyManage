# !/bin/bash 
pwd
#sudo docker build -t pyinstaller ~/.local/bin/nylinuxUtil/lib/DockerBuilder
if [ -d ./.env/ ]; then
    source ./.env/bin/activate
fi

pip install requests
pip freeze > requirements.txt

sudo docker run -it -v $(pwd):/src pyinstaller $@
echo "Build complete"
echo Start assembly pakage

python  ~/.local/bin/nylinuxUtil/ny/build.py


