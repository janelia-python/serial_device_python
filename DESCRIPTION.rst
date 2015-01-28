serial_device_python
====================

This Python package (serial_device2) creates a class named
SerialDevice, which inherits from serial.Serial and adds methods to
it, like auto discovery of available serial ports in Linux, Windows,
and Mac OS X. The SerialDevice class can be used by itself, but it is
mostly intended to be a base class for other serial port devices with
higher level functions.

Authors::

    Peter Polidoro <polidorop@janelia.hhmi.org>

License::

    BSD

Example Usage::

    from serial_device2 import SerialDevice, find_serial_device_ports
    find_serial_device_ports() # Returns list of available serial ports
    dev = SerialDevice()  # Automatically finds device if one available
    dev.get_device_info()
    dev = SerialDevice('/dev/ttyACM0') # Linux
    dev = SerialDevice('/dev/tty.usbmodem262471') # Mac OS X
    dev = SerialDevice('COM3') # Windows
    devs = SerialDevices()  # Automatically finds all available devices
    devs.get_devices_info()
    devs.sort_by_port()
    dev = devs[0]
    dev.get_device_info()

