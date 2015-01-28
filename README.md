serial_device_python
====================

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
from serial_device2 import SerialDevice, SerialDevices, find_serial_device_ports
find_serial_device_ports() # Returns list of available serial ports
dev = SerialDevice()  # Automatically finds device if one available
dev = SerialDevice('/dev/ttyACM0') # Linux
dev = SerialDevice('/dev/tty.usbmodem262471') # Mac OS X
dev = SerialDevice('COM3') # Windows
devs = SerialDevices()  # Automatically finds all available devices
devs.get_devices_info()
devs.sort_by_port()
dev = devs[0]
dev.get_device_info()
```

##Installation

###Linux and Mac OS X

[Setup Python for Linux](./PYTHON_SETUP_LINUX.md)

[Setup Python for Mac OS X](./PYTHON_SETUP_MAC_OS_X.md)

```shell
mkdir -p ~/virtualenvs/serial_device2
virtualenv ~/virtualenvs/serial_device2
source ~/virtualenvs/serial_device2/bin/activate
pip install serial_device2
```

###Windows

[Setup Python for Windows](./PYTHON_SETUP_WINDOWS.md)

```shell
virtualenv C:\virtualenvs\serial_device
C:\virtualenvs\serial_device\Scripts\activate
pip install serial_device2
```
