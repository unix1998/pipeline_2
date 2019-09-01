#!/usr/local/bin/python3

import datetime
import zipfile
import glob 
import os
import sys
import logging 
import wx
import time

class StreamToLogger(object):
   
   #Fake file-like stream object that redirects writes to a logger instance.
   
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''

   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())
today1=datetime.datetime.now().strftime("%Y-%m-%d")
out_file_name="/home/opt/app1“+today1
logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   filename=out_file_name,
   filemode='a'
)

stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, logging.INFO)
sys.stdout = sl

stderr_logger = logging.getLogger('STDERR')
sl = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = sl

print ("Test to standard out")


print ("test1234")
