python_serial_device
====================

This Python package creates a class named SerialDevice, which inherits
from serial.Serial and adds methods to it, like auto discovery of
available serial ports in Linux, Windows, and Mac OS. The SerialDevice
class can be used by itself, but it is mostly intended to be a base
class for other serial port devices with higher level functions.

Authors:
Peter Polidoro <polidorop@janelia.hhmi.org>

##Example Usage


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
