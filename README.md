python_serial_device
====================

##Usage


```python
from serial_device import SerialDevice, find_serial_device_ports
find_serial_device_ports()
dev = SerialDevice()
dev.get_serial_device_info()
```

##Installation

###Linux and Mac OS

```shell
mkdir -p ~/virtualenvs/serial_device
virtualenv ~/virtualenvs/serial_device
source ~/virtualenvs/serial_device/bin/activate
pip install https://github.com/JaneliaSciComp/python_serial_device/tarball/master
```

###Windows

Download Python 2.7.8 Windows Installer from:

    https://www.python.org/download

Add to path:

    C:\Python27\

Download get-pip.py from:

    https://bootstrap.pypa.io/get-pip.py

Run:

```shell
python get-pip.py
```

Add to path:

    C:\Python27\Scripts\

Run:

```shell
pip install virtualenv
mkdir C:\virtualenvs
virtualenv C:\virtualenvs\serial_device
C:\virtualenvs\serial_device\Scripts\activate
pip install https://github.com/JaneliaSciComp/python_serial_device/zipball/master
```
