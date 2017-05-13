# coding: utf-8
import sys
import time
try:
    x = input('Input :')
    print(float(x))
except:
    print("Error! Try again.")
    x = input('Input :')
y = input('keep calcurating → 0 , exit → 1:')
while y == 0:
    try:
        x = input('Input :')
        print(float(x))
    except:
        print("Error! Try again.")
    y = input('keep calcurating → 0 , exit → 1:')
if y == 1:
    print("Good bye")
    sys.exit()
else:
    print("Error! This application has stopped.")
    sys.exit()
