import subprocess
from timeout import timeout
import errno
import os


class Executor:

  def __init__(self):
    pass

  # Execute a command and returns the output, timeout after 15 minutes
  @staticmethod
  @timeout(900)
  def execute(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = proc.communicate()[0]
    return out.rstrip()

  # Execute a shell command and return the return_code, timeout after 15 minutes
  @staticmethod
  @timeout(900)
  def execute_output(cmd):
    proc = subprocess.Popen(cmd, shell=True)
    proc.communicate()
    return proc.returncode

  #Execute a shell command without timeout
  @staticmethod
  def execute_output_without_timeout(cmd):
    proc = subprocess.Popen(cmd, shell=True)
    proc.communicate()
    return proc.returncode
