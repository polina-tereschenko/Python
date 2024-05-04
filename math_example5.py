from math import *
str = float (input("Введіть число:"))
x = float(str)
if x <= -6:
    y = 2
if x >= -6 and x > -2:
    y = -(1+6) * (x*(1+6))
if x >= -2 and x < 0:
    y = -sqrt (4-x ** 2)
if x >= 0 and x < 2:
    y = sqrt (4-x ** 2)
if x >= 0 and x < 2:
    y = 5 * x+2
print ("X = {0: .2f} Y ={1: .2f}".format (x, y))
