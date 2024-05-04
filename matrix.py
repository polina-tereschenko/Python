n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        num = float(input("Введіть число [{}, {}]: ".format(i, j)))
        while num < -10 or num > 10:
            print("Числа повинні бути від -10 до 10.")
            num = float(input("Введіть число [{}, {}]: ".format(i, j)))
        row.append(num)
    matrix.append(row)

min_row_index = 0
min_element = matrix[0][0]
for i in range(n):
    for j in range(m):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_row_index = i

matrix[0], matrix[min_row_index] = matrix[min_row_index], matrix[0]

for row in matrix:
    print(row)
