# Задача №9
# # По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Input:       5
# Output:    120

n = int(input("Введите ваше число: "))
i = 1
N = 1

while i <= n:
    N *= i
    i += 1

print(N)

# Задача №11.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

A = int(input("Введите ваше число: "))
f1, f2 = 0, 1
n = 2

while f2 < A:
    f1, f2 = f2, f1 + f2
    n += 1

if f2 == A:
    print(n)
else:
    print(-1)