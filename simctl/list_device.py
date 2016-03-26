import json
from device import Device
from device_type import DeviceType
from executor import Executor
from runtime import RunTime

CMD = 'xcrun simctl list -j {0}'


class ListDevice:

  def device(self, filter_func):
    return filter(filter_func, self.list_devices())[:1]

  def device_type(self, filter_func):
    return filter(filter_func, self.list_device_types())[:1]

  def runtime(self, filter_func):
    return filter(filter_func, self.list_runtimes())[:1]

  def list_devices(self):
    output = Executor.execute(CMD.format('devices'))
    os_device_list = json.loads(output)['devices']
    device_array = []
    for os in os_device_list:
      device_array += [Device(device_dict['availability'],
                       device_dict['name'],
                       os,
                       device_dict['state'],
                       device_dict['udid']
                       ) for device_dict in os_device_list[os]]
    return device_array

  def list_device_types(self):
    output = Executor.execute(CMD.format('devicetypes'))
    device_type_list = json.loads(output)['devicetypes']
    return [DeviceType(device_type['identifier'], device_type['name']) for device_type in device_type_list]


  def list_runtimes(self):
    output = Executor.execute(CMD.format('runtimes'))
    runtime_list = json.loads(output)['runtimes']
    return [RunTime(runtime['availability'],
                    runtime['buildversion'],
                    runtime['identifier'],
                    runtime['name'],
                    runtime['version']) for runtime in runtime_list]




