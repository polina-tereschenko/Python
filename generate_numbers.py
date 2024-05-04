import random

def generate_positive_integer_numbers(N):
    return [random.randint(0, 50) for _ in range(N)]

def bubble_sort(lst):
    N = len(lst)
    for i in range(N-1):
        for j in range(N-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
n = input("Введіть значення n:")
N = int(n)
list_a = generate_positive_integer_numbers(N)
bubble_sort(list_a)
print(list_a)