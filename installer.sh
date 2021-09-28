# !bin/bash

cp -r ./lib ~/.local/bin/nylinuxUtil
cp -r ./ny ~/.local/bin/nylinuxUtil
cp -r ./ref ~/.local/bin/nylinuxUtil
if ! [ -f ~/.local/bin/nylinuxUtil/base.json ]; then
    cp ./base.json ~/.local/bin/nylinuxUtil/base.json
fi


#sudo docker pull kicsikrumpli/wine-pyinstaller

#docker build -t kicsikrumpli/wine-pyinstaller:latest .

#sudo docker build -t pyinstaller ~/.local/bin/nylinuxUtil/lib/DockerBuilder

echo "alias nys='python ~/.local/bin/nylinuxUtil/ny/nys.py \$@'" >> ~/.bashrc
echo "alias nyb='python ~/.local/bin/nylinuxUtil/ny/nyb.py \$@'" >> ~/.bashrc
source ~/bashrc