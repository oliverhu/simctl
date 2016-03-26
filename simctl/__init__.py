"""
The simctl moduls is a wrapper of xcode toolchains's simctl command.
Also a port of ruby gem SimCtl to Python.
"""

from device_type import DeviceType
from executor import Executor
from list_device import ListDevice
from device import Device

DEVICE_LIST = ListDevice()


class SimCtl:

  @staticmethod
  def create_device(name, device_type, runtime):
    cmd = 'xcrun simctl create "{0}" "{1}" "{2}"'.format(name, device_type.identifier, runtime.identifier)
    uuid = Executor.execute(cmd)
    device = Device(uuid=uuid, name=name)
    return device

  @staticmethod
  def launch_device(device):
    xcode_address = Executor.execute('xcode-select -p')
    cmd = "open -n {0}/Applications/Simulator.app --args -ConnectHardwareKeyboard 0 -CurrentDeviceUDID {1}".format(xcode_address, device.uuid)
    Executor.execute(cmd)

  @staticmethod
  def boot_device(device):
    cmd = 'xcrun simctl boot {0}'.format(device.uuid)
    Executor.execute(cmd)

  @staticmethod
  def delete_device(device):
    cmd = 'xcrun simctl delete {0}'.format(device.uuid)
    Executor.execute(cmd)

  @staticmethod
  def install_device(device, app_path):
    cmd = 'xcrun simctl install {0} {1}'.format(device.uuid, app_path)
    Executor.execute(cmd)

  @staticmethod
  def kill_device(device):
    cmd = "ps xww | grep Simulator.app | grep -s {0} | grep -v grep | awk '{{print $1}}'".format(device.uuid)
    output = Executor.execute(cmd)
    if output == '':
      return
    pid = int(output)
    if pid > 0:
      Executor.execute('kill {0}'.format(pid))

  @staticmethod
  def erase_device(device):
    cmd = 'xcrun simctl erase {0}'.format(device.uuid)
    Executor.execute(cmd)

  @staticmethod
  def shutdown_device(device):
    cmd = 'xcrun simctl shutdown {0}'.format(device.uuid)
    Executor.execute(cmd)

  @staticmethod
  def reset_device(name, device_type, runtime):
    for device in filter(lambda device: device.name == name and device.os == runtime.name, DEVICE_LIST.list_devices()):
      device.kill()
      device.shutdown()
      device.delete()
    return SimCtl.create_device(name, device_type, runtime)




