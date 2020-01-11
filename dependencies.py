#!/usr/bin/python3
from sys import version_info
from os import system, geteuid

if geteuid() != 0:
    print("rerun as root")
    exit()

system("apt-get install python3 python3-dev python3-pip libbluetooth-dev libreadline-dev libboost-python-dev "
       "libboost-thread-dev -y")


# https://stackoverflow.com/questions/41463847/got-error-while-download-gattlib-via-pip3
v = '{0}{1}'.format(version_info[0], version_info[1])
print("installing for python version {0}".format(v))
system("cd /tmp/;"
       "pip3 download gattlib;"
       "tar xvzf ./gattlib-0.20150805.tar.gz;"
       "cd gattlib-0.20150805/;"
       "sed -ie 's/boost_python-py34/boost_python{0}/' setup.py;"
       "pip3 install .;"
       "cd ..;"
       "rm -rf gattlib-0.20150805/".format(v))


system("pip3 install -r requirements.txt")
