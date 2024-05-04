n = int(input("Введіть число від 1 до 9: "))
i = 1
f = n
while i <= n:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1
i = n - 1
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i -= 1
print('1')