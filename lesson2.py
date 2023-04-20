### Списки


list_1 = [] # 1-й вариант создания пустого списка
list_1 = list() # 2-й вариант создания пустого списка
list_1 = [1, 3, 5, 8] # объявление элементов списка
print(*list_1) # * убирает квадратные скобки при выводе списка

for i in list_1:
    print(i)    # цикл отображает все элементы списка по очереди

print(len(list_1)) # отображение длины списка

print(list_1[1]) # обращение к элементу списка по индексу 1
print(list_1[-1]) # так отобразится первый элемент с конца

list_1 = [1, 5]
print(list_1)
list_1.append(8) # добавили 8 в конец списка
print(list_1)

# цикл - добавление новых элементов в список
list_1 = []
for i in range(5): 
    list_1.append(i)
    print(list_1)

# удаление элементов списка с конца
list_1 = [12, 7, -1, 21, 0]
a = list_1.pop()
print(a) # pop также может и возвращать удаляемый элемент 
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)

# удаление конкретного элемента из списка (по индексу)
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(1))
print(list_1)

# добавление элемента на нужную позицию
list_1 = [4, 90, -3, 23, 7]
print(list_1.insert(2, 11)) # 1-й аргумент - позиция, 2-й аргумент - значение
print(list_1)

# Срезы:

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1)
print(list_1[0])    # 1
print(list_1[0])    # 2
print(list_1[len(list_1)-1])    # 10
print(list_1[-5])   # 6
print(list_1[:])    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])   # [1, 2] вывод от начала до второго индекса
print(list_1[len(list_1)-2:])   # [9, 10] вывод от минус второго элемента с конца и до конца
print(list_1[2:9])  # [2, 3, 4, 5, 6, 7, 8, 9] вывод от 2-го по 9-й индекс
print(list_1[6:-18])    # []
print(list_1[0:len(list_1):6])  # [1, 7] вывод от начала до конца с шагом 6
print(list_1[::6])  # аналогичен предыдущему [1, 7] вывод от начала до конца с шагом 6

### Кортежи

t = ()      # пустой кортеж
print(type(t))

t = (1, 5, 3,)
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)    # преобразование списка в кортеж с сохранением элементов в нем
print(v)
print(type(v))

a, b, c = v     # разъединение кортежа на 3 переменные
print(a, b, c)

x = y = 1
x, y = 1, 2 


t = (1, 2, 3, 5,)
print(t[1])

for i in range(len(t)):
    print(t[i])

### Словари

d = {}  #
d = dict()  #

d['q'] = 'qwerty'
d['w'] = 'werty'
print(d['q'])

dictionary = {}
dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}

del dictionary['left']  # удаление элемента по ключу

# порядок выведения ключ:значение
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))

# альтернативный вариант
for (k, v) in dictionary.items():
    print(k, v)

print(dictionary.items())

### Множества

colors = {'red', 'green', 'blue'}
print(colors)   # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)   # {'grey', 'red', 'green', 'blue'}
colors.remove('red')
print(colors)   # {'grey', 'green', 'blue'}
colors.discard('red')   # проверяет если такое значение есть во множестве и удаляет его
print(colors)   # {'grey', 'green', 'blue'}
colors.clear()
print(colors) # set()

# Операции со множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()    # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21} объединение
i = a.intersection(b)   # {8, 2, 5} пересечение элементов
d1 = a.difference(b)    # {1, 3} разность элементов
d2 = b.difference(a)    # {13, 21}
q = a.union(b).difference(a.intersection(b))    # {1, 21, 3, 13} сначала действие в скобках - найти пересечение а и b; затем а объединяем с b; из полученного множества находим разность

a = {1, 8, 6}
b = frozenset(a)    # множество которое невозможно изменить
print(b)

### List comprehension - генератор списка

# list_1 = [exp for item in iterable]
# list_1 = [exp for item in iterable (if conditional)]

# Задача: 
# Создать список, состоящий из четных чисел в диапазоне 1...100
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [1, 2, 3,...,100]

# создать пары каждому из чисел
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]

# умножить значение на 2
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]

print(list_1[1]) # обращение к элементу списка по индексу 1
