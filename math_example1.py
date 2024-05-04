import math

x = float(input('Enter your number: '))

if (x <= 0) :
    y = math.sqrt(1 + x ** 2 - math.cos ** 2 * x)
else:
    y = (x / 3 ** math.sqrt(math.e ** x+1))

print('x = ', x, 'y = ', y)