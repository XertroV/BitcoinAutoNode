#!/bin/bash

apt-get -y update
apt-get -y install screen
wget https://raw.github.com/XertroV/BitcoinAutoNode/master/bitcoinAutoNode.sh
screen -dmS bitcoinInstaller sudo bash bitcoinAutoNode.sh
