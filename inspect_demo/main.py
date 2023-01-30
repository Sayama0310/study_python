# import required module
import inspect
import pprint
import math


# create classes
class A(object):
    pass


class B(A):
    pass


class C(B):
    pass


def fun(a, b):
    # product of
    # two numbers
    return a * b


# nested list of tuples
print(inspect.getmro(C))
pprint.pp(inspect.getclasstree(inspect.getmro(C)))
pprint.pp(inspect.getmembers(math))
pprint.pp(inspect.signature(pprint.pp))
print(inspect.getsource(fun))
print(inspect.getmodule(math))

from tkinter import *

# create object
root = Tk()

# use getdoc()
print(inspect.getdoc(root))
