## pybt
[![Build Status](http://build.eberlein.io:8080/job/pybt/badge/icon)](http://build.eberlein.io:8080/job/pybt/)

### how to ...
#### ... get started
```bash
./dependencies.sh
pip install .
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
classic A8:B8:6E:C1:6A:28 Nexus 5X
	services: 15
```

or check [bt.py](https://github.com/smthnspcl/pybt/blob/master/bt.py)