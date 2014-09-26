'''
This Python package (serial_device2) creates a class named SerialDevice,
which inherits from serial.Serial and adds methods to it, like auto
discovery of available serial ports in Linux, Windows, and Mac OS X. The
SerialDevice class can be used by itself, but it is mostly intended to
be a base class for other serial port devices with higher level
functions. SerialDevices creates a list of SerialDevice
instances from all available serial ports.
'''
from serial_device2 import SerialDevice, SerialDevices, find_serial_device_ports, find_serial_device_port, WriteFrequencyError, __version__
