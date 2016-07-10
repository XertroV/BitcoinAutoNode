BitcoinAutoNode
===============

A script to run (ideally just after starting up a new server/vps) to automatically setup `bitcoind` and have it start on boot.

This script runs `bitcoind` under the `bitcoin` user. An alias (`btc`) is added to the current user's `.bashrc`. Where you'd normally type `bitcoin-cli` you can type `btc`, eg: `btc getinfo`.

It has been tested on Ubuntu Server 14.04 and 15.04. It is intended for use only on these distros.

One Liner
---------

    wget https://raw.github.com/XertroV/BitcoinAutoNode/master/bitcoinAutoNode.sh ; sudo bash bitcoinAutoNode.sh

You should really check out the code before running that though.

### Super Lazy Method

If you want to run one command then disconnect (nearly) straight away, use this:

    wget https://raw.github.com/XertroV/BitcoinAutoNode/master/stub.sh ; sudo bash stub.sh ; exit

It should drop the connection once it's started. You can view the setup with `screen -r bitcoinInstaller` and detach (when viewing) with `Ctrl+a d`.


Notes
-----

Previously, the script would prompt you to change your password and would install the ufw (and allow ports 8333 and 22). However, I've removed that. All that happens now is installing `bitcoind` and dependencies.

Pruning is used and by default set to a maximum of ~60% of the `/` volume, ensuring it can be run on a small VPS. For this reason a 2 GB swap file is also instantiated.
