# !bin/bash

cp -r ./ ~/.local/bin/nylinuxUtil

echo "alias nys='python ~/.local/bin/nylinuxUtil/ny/nys.py \$@'" >> ~/.bashrc
echo "alias nyb='python ~/.local/bin/nylinuxUtil/ny/nyb.py \$@'" >> ~/.bashrc