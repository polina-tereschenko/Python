import math

n = int(input("Введіть натуральне число: "))
total = 0
for i in range(1, n+1):
    if i == 1:
        total += (1/math.sqrt(1))
    else:
        d = sum(math.sqrt(j) for j in range(1, i))
        total += (-1)**(i+1)/d
print(total)