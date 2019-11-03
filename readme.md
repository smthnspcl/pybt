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

pip3 install -r requirements.txt
```

#### ... to use it
```
Python 3.7.5rc1 (default, Oct  8 2019, 16:47:45) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.9.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from pybt import Scanner, ClassicDevice                                                                                                                                        

In [2]: Scanner.scan_for()                                                                                                                                                             
Permission Denied
Set scan parameters failed (are you root?)
found 1 devices
Out[2]: [<pybt.libs.bt.classic.ClassicDevice at 0x7f3427045210>]

In [3]: c = ClassicDevice.scan()                                                                                                                                                       

In [4]: c                                                                                                                                                                              
Out[4]: [<pybt.libs.bt.classic.ClassicDevice at 0x7f3425559d50>]

In [5]: c[0].__dict__                                                                                                                                                                  
Out[5]: 
{'address': 'A8:B8:6E:C1:6A:28',
 'timestamp': '03.11.2019 16:48:06',
 'name': 'Nexus 5X'}

```

or check [bt.py](https://github.com/smthnspcl/pybt/blob/master/bt.py)