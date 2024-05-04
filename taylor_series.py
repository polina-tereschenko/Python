import math

def taylor_series_sqrt(x, n):
    result = 0
    power = 0.5

    for i in range(n):
        term = x ** power
        result += term
        power += 2

    return result

def taylor_series_root(x, n):
    result = 0
    power = 1

    for i in range(n):
        term = (x ** power) / ((1 - x) ** 2)
        result += term
        power += 2

    return result

x = float(input("Введіть значення x: "))

n = int(input("Введіть кількість членів ряду: "))

sqrt_series = taylor_series_sqrt(x, n)

root_series = taylor_series_root(x, n)

print("Розкладання x^(1/2) + x^(5/2) + x^(9/2) + ...: ", sqrt_series)
print("Розкладання корінь x/(1-x)^2: ", root_series)
