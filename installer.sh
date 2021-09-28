# !bin/bash

cp -r ./ ~/.local/bin/nylinuxUtil

sudo docker pull kicsikrumpli/wine-pyinstaller

docker build -t kicsikrumpli/wine-pyinstaller:latest .

sudo docker build -t pyinstaller ~/.local/nylinuxUtil/lib/DockerBuilder

echo "alias nys='python ~/.local/bin/nylinuxUtil/ny/nys.py \$@'" >> ~/.bashrc
echo "alias nyb='python ~/.local/bin/nylinuxUtil/ny/nyb.py \$@'" >> ~/.bashrc