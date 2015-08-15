#!/bin/bash
echo "########### The server will reboot when the script is complete"
echo "########### Changing to home dir"
cd ~
echo "########### Updating Ubuntu"
apt-get -y update
apt-get -y upgrade
apt-get -y dist-upgrade
apt-get -y install software-properties-common python-software-properties htop
apt-get -y install git build-essential autoconf libboost-all-dev libssl-dev pkg-config
apt-get -y install libprotobuf-dev protobuf-compiler libqt4-dev libqrencode-dev libtool
apt-get -y install libcurl4-openssl-dev

echo "########### Creating Swap"
dd if=/dev/zero of=/swapfile bs=1M count=2048 ; mkswap /swapfile ; swapon /swapfile
echo "/swapfile swap swap defaults 0 0" >> /etc/fstab

echo "########### Adding ppa:bitcoin/bitcoin and installing db4.8"
add-apt-repository -y ppa:bitcoin/bitcoin
apt-get update -y
apt-get -y install db4.8

echo "########### Cloning XT and Compiling"
mkdir -p ~/src && cd ~/src
git clone https://github.com/bitcoinxt/bitcoinxt.git
cd bitcoinxt
./autogen.sh
./configure --without-gui --without-upnp --disable-tests
make
make install

echo "########### Create Bitcoin User"
useradd -m bitcoin

echo "########### Creating config"
cd ~bitcoin
sudo -u bitcoin mkdir .bitcoin
config=".bitcoin/bitcoin.conf"
sudo -u bitcoin touch $config
echo "server=1" > $config
echo "daemon=1" >> $config
echo "connections=40" >> $config
randUser=`< /dev/urandom tr -dc A-Za-z0-9 | head -c30`
randPass=`< /dev/urandom tr -dc A-Za-z0-9 | head -c30`
echo "rpcuser=$randUser" >> $config
echo "rpcpassword=$randPass" >> $config

# set prune amount to size of `/` 75% (and then by /1000 to turn KB to MB) => /1333
echo "prune="$(expr $(df | grep '/$' | tr -s ' ' | cut -d ' ' -f 2) / 1333) >> $config # safe enough for now

echo "########### Setting up autostart (cron)"
crontab -l > tempcron
echo "0 3 * * * reboot" >> tempcron  # reboot at 3am to keep things working okay
crontab tempcron
rm tempcron

# only way I've been able to get it reliably to start on boot
# (didn't want to use a service with systemd so it could be used with older ubuntu versions, but systemd is preferred)
sed -i '2a\
sudo -u bitcoin /usr/local/bin/bitcoind' /etc/rc.local

reboot
