python_serial_device
====================

This Python package creates a class named SerialDevice, which inherits
from serial.Serial and adds methods to it, like auto discovery of
available serial ports in Linux, Windows, and Mac OS. The SerialDevice
class can be used by itself, but it is mostly intended to be a base
class for other serial port devices with higher level functions.

Authors:
Peter Polidoro <polidorop@janelia.hhmi.org>

License:
BSD

Example Usage::

    from serial_device import SerialDevice, find_serial_device_ports
    find_serial_device_ports()
    dev = SerialDevice()
    dev.get_serial_device_info()

