### Функции

def sum_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum_numbers(5))

a = sum_numbers(3)
print(a)

def sum_str(*args): # *args позволяет задавать неограниченное к-во аргументов
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))


## Модульность

import module # импорт всего файла
from module import max1 # импорт определенной функции
from module import * # импорт всех функций
import module as m1 # импорт модуля и изменение его названия для удобства

print(module.max1(5, 9))
print(m1.max1(5, 9))

### Рекурсия

# если число n равно 1 или 2, это означает, что первое число и второе число последовательности равны 1. Мы так и делаем возвращаем 1
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

### Алгоритмы

# Быстрая сортировка
def quick_sort(array):
    if len(array) <= 1: # базис, то место где рекурсия будет завершать работу
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14, 5, 9, 2, 0, 2, 10]))


# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1, 5, 4, 3, 8, 1, 30, 2]
merge_sort(list_1)
print(list_1)

