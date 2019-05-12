#!/usr/local/bin/python3
def addspam(fn):
     def new(*args):
         print ("spam, spam, spam")
         return fn(*args)
     return new

# @addspam
if __name__ == "__main__":
 a = 3 +5 
 print (a)
