BitcoinAutoNode
===============

A script to run (ideally just after starting up a new server/vps) to automatically setup bitcoind and have it start on boot.

This script will run `bitcoind` as root, which is not advised in production environments. This script should be educational, or used only to create a dedicated node.

It has been tested on Ubuntu Server 14.04 and 15.04. It is intended for use only on these distros.

One Liner
---------

    wget https://raw.github.com/XertroV/BitcoinAutoNode/master/bitcoinAutoNode.sh ; sudo bash bitcoinAutoNode.sh

You should really check out the code before running that though.

Notes
-----

Currently Bitcoin XT is cloned from git and compiled. If you would like to set use Bitcoin Core instead you can find the last version to support installing from PPA [here](https://raw.githubusercontent.com/XertroV/BitcoinAutoNode/792d059a65dd240ce5c952653207272c7f1246c2/bitcoinAutoNode.sh).

Previously, the script would prompt you to change your password and would install the ufw (and allow ports 8333 and 22). However, I've removed that. All that happens now is installing `bitcoind` and dependencies.

Pruning is used and by default set to a maximum of ~75% of the `/` volume, ensuring it can be run on a small VPS. For this reason a 2 GB swap file is also instantiated.
