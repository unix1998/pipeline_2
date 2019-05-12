#! /usr/bin/python
class animal():
 name="hh"
 sex="man"
 def __init__(self):
  self.height=10
  self.weight=50
 def deception(self):
  print "ansible.height:"+self.height+" animal.weight:"+self.weight
 def run(self):
  print "animal is running...."
class dog(animal):
 def __init__(self):
  pass
if __name__=="__main__":
 dg=dog()
 print dg.__dict__
