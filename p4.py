#!/usr/local/bin/python3
def f1(arg):
    print ("f1")
    rl = arg()
    print (rl)
    return rl + "f1"

@f1
def f2(arg = ""):
    print ("f2")
    return arg + "f2r"

print ("start")
print (f2)
