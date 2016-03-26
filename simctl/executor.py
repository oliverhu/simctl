import subprocess
from ios_runner.timeout import timeout
import errno
import os


class Executor:

  def __init__(self):
    pass

  @staticmethod
  @timeout(900)
  def execute(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = proc.communicate()[0]
    return out.rstrip()

  @staticmethod
  @timeout(900)
  def execute_output(cmd):
    proc = subprocess.Popen(cmd, shell=True)
    proc.communicate()
    return proc.returncode

  @staticmethod
  def execute_output_without_timeout(cmd):
    proc = subprocess.Popen(cmd, shell=True)
    proc.communicate()
    return proc.returncode
