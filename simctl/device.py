import simctl


class Device:

  def __init__(self, uuid, availability='', name='', os='', state=''):
    self.availability = availability
    self.name = name
    self.os = os
    self.state = state
    self.uuid = uuid
    self.target = ""

  def install(self, app_path):
    simctl.SimCtl.install_device(self, app_path)

  def boot(self):
    simctl.SimCtl.boot_device(self)

  def delete(self):
    simctl.SimCtl.delete_device(self)

  def erase(self):
    simctl.SimCtl.erase_device(self)

  def kill(self):
    simctl.SimCtl.kill_device(self)

  def launch(self):
    simctl.SimCtl.launch_device(self)

  def shutdown(self):
    simctl.SimCtl.shutdown_device(self)
