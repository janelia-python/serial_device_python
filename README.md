#serial_device_python

This Python package (serial_device2) creates a class named
SerialDevice, which inherits from serial.Serial and adds methods to
it, like auto discovery of available serial ports in Linux, Windows,
and Mac OS X. The SerialDevice class can be used by itself, but it is
mostly intended to be a base class for other serial port devices with
higher level functions. SerialDevices creates a list of SerialDevice
instances from all available serial ports.

Authors:

    Peter Polidoro <polidorop@janelia.hhmi.org>

License:

    BSD

##Example Usage


```python
from serial_device2 import SerialDevice, find_serial_device_ports
find_serial_device_ports() # Returns list of available serial ports
dev = SerialDevice() # Might automatically find device if one available
# if it is not found automatically, specify port directly
dev = SerialDevice(port='/dev/ttyUSB0') # Linux
dev = SerialDevice(port='/dev/tty.usbmodem262471') # Mac OS X
dev = SerialDevice(port='COM3') # Windows
dev.get_device_info()
```

```python
from serial_device2 import SerialDevices
devs = SerialDevices()  # Might automatically find all available devices
# if they are not found automatically, specify ports to use
devs = SerialDevices(use_ports=['/dev/ttyUSB0','/dev/ttyUSB1']) # Linux
devs = SerialDevices(use_ports=['/dev/tty.usbmodem262471','/dev/tty.usbmodem262472']) # Mac OS X
devs = SerialDevices(use_ports=['COM3','COM4']) # Windows
devs.get_devices_info()
devs.sort_by_port()
dev = devs[0]
dev.get_device_info()
```

##Installation

[Setup Python](https://github.com/janelia-pypi/python_setup)

###Linux and Mac OS X

```shell
mkdir -p ~/virtualenvs/serial_device2
virtualenv ~/virtualenvs/serial_device2
source ~/virtualenvs/serial_device2/bin/activate
pip install serial_device2
```

###Windows

```shell
virtualenv C:\virtualenvs\serial_device
C:\virtualenvs\serial_device\Scripts\activate
pip install serial_device2
```
