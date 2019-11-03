## pybt
[![Build Status](http://build.eberlein.io:8080/job/pybt/badge/icon)](http://build.eberlein.io:8080/job/pybt/)

### how to ...
#### ... get started
```shell script
sudo apt install python3 python3-dev python3-pip libbluetooth-dev \
                 libreadline-dev libboost-python-dev libboost-thread-dev -y

# https://stackoverflow.com/questions/41463847/got-error-while-download-gattlib-via-pip3
pip3 download gattlib
tar xvzf ./gattlib-0.20150805.tar.gz
cd gattlib-0.20150805/
# edit your py version accordingly
sed -ie 's/boost_python-py34/boost_python37/' setup.py
pip3 install .


```

#### ... to use it
```
Python 3.6.8 (default, Aug 20 2019, 17:12:48) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from pybt.bt import Scanner                                                                                                                                                               

In [2]: s = Scanner()

In [3]: s.print_devices(s.scan_for())                                                                                                                                                             
Permission Denied
Set scan parameters failed (are you root?)
found 1 devices
------------------------------------------
classic A8:B8:6E:C1:XX:XX Nexus 5X
	services: 15
```

or check [bt.py](https://github.com/smthnspcl/pybt/blob/master/bt.py)