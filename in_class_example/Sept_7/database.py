#database.py
print("This is the database.py module")
print("Pyton thinks this is called {}".format(__name__))

from interface import *
# from numpy import *
import math as m

answer = check_HDL(55)
print("The HDL of 55 is {}".format(answer))