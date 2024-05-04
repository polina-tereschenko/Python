import math

def f(x):
   return math.sinh(x) * math.sqrt(x)

k = 0.1
m = 0.1
n = 0.5

x = m

while x <= n:
    y = f(x)
    print("f({}) = {}".format(x, y))
    x += k