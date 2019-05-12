#!/usr/local/bin/python3
def addspam(fn):
     def new(*args):
         print ("spam, spam, spam")
         
         return fn(*args)
     return new

@addspam
def useful(a, b):
     print (a**2 + b**2)
     print ("tttttttttttttttttttttttttt")
if __name__ == "__main__":
   useful(3,4)
#  a = 3 +5 
#  print (a)
   #addspam("abc")
   #addspam("useful")
