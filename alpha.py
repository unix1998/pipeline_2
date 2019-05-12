#!/usr/local/bin/python3
def funcA(A):
    print("function A")

def funcB(B):
    print(B(2))
    print("function B")

@funcA
@funcB
def func(c):
    print("function C")
    return c**2

if __name__=="__main__i":
   func(7)


