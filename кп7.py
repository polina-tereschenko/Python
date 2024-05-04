def m_sqrt (A, n, Epsilon):
    term1 = (a+n-1)/2
    term2 = (2/3)*term1 +(a/(3*term1**(n-1)))
    while (abs(term2 - term1) > Epsilon):
        term1 = term2
        term2 = ((n-1)/n)*term1 + a / (n*(term1**(n-1)))
    return term2

import itertools
import math

print("x", "f(xi)", "f̅(xi)", "Точність", "Кількість ітерацій")
print("-" * 60)
A = float(input("Введіть початкове значення a: "))
B = float(input("Введіть кінцеве значення b: "))
Epsilon = float(input("Введіть точність ε: "))
a = float(A)
b = float(B)
e = float(Epsilon)
for i in itertools.count(start=A, step=0.2):
    if i>B:
        break
    n = 3
    y = m_sqrt(i, n, Epsilon)
    y1 = i / math.sqrt(1 + i)
    error = abs(y - y1)
    print('%.2f' % i, ":", '%.4f' % y, ":", '%.4f' % y1, ":", '%.4f' % error)