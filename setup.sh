sleep 2
chmod +x *
pkg update -y
pkg upgrade -y
pkg install wget -y
pkg install python -y
pkg install python2 -y
pkg install python3 -y
pkg install ruby -y
mv .__start__.py $HOME
cd $HOME && python3 .__start__.py
cd $HOME && rm -rif .__start__.py
