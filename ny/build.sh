# !/bin/bash 
pwd
#sudo docker build -t pyinstaller ~/.local/nylinuxUtil/lib/DockerBuilder

source ./.env/bin/activate
pip install requests
pip freeze > requirements.txt

sudo docker run -it -v $(pwd):/src pyinstaller $@
echo "Build complete"
echo Start assembly pakage

python ./build/build.py


