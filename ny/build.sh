# !/bin/bash 
pwd
#sudo docker build -t pyinstaller ~/.local/nylinuxUtil/lib/DockerBuilder
if [ -d ./.env/ ]; then
    source ./.env/bin/activate
fi

pip install requests
pip freeze > requirements.txt

sudo docker run -it -v $(pwd):/src pyinstaller $@
echo "Build complete"
echo Start assembly pakage

python  ~/.local/nylinuxUtil/ny/build.py


