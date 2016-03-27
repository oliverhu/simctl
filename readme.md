# simctl

[![Build Status](https://travis-ci.org/oliverhu/simctl.svg?branch=master)](https://travis-ci.org/oliverhu/simctl)

Python interface to xcrun simctl. Manage your iOS Simulators directly from a python script. This can be helpful for testing on different Simulators. This is a port from plu's Ruby version of [simctl](https://github.com/plu).

## Usage

```python
from simctl import SimCtl
# Select the iOS 9.2 runtime
runtime = SimCtl.runtime(name: 'iOS 9.2')

# Select the iPhone 5 device type
devicetype = SimCtl.devicetype(name: 'iPhone 5')

# Create a new device
device = SimCtl.create_device('Unit Tests @ iPhone 5 9.2', devicetype, runtime)

# Launch a new Simulator.app instance
device.launch()

# Kill the Simulator.app instance again
device.kill()

# Delete the device
device.delete()

```
