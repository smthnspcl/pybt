#!/usr/bin/env bash

sudo apt install python3 python3-dev python3-pip libbluetooth-dev libreadline-dev libboost-python-dev libboost-thread-dev -y
cd /tmp/
pip3 download gattlib
tar xvzf ./gattlib-0.20150805.tar.gz
cd gattlib-0.20150805/
sed -ie 's/boost_python-py34/boost_python-py36/' setup.py
pip3 install .