# Задача 2:
# Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Enter a three-digit number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("The sum of the digits is:", sum)

# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = int(input("Enter the total number of cranes: "))
x = S // 6

petya = x
seryozha = x

katya = (petya + seryozha) * 2

print("Petya made", petya, "cranes.")
print("Katya made", katya, "cranes.")
print("Seryozha made", seryozha, "cranes.")

# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

num = input("Enter a 6-digit number: ")

# Check if the input has exactly 6 digits
if len(num) != 6:
    print("Error: Input must have exactly 6 digits")
else:
    first_three = int(num[0]) + int(num[1]) + int(num[2])
    last_three = int(num[3]) + int(num[4]) + int(num[5])
    
    if first_three == last_three:
        print("The ticket is lucky")
    else:
        print("The ticket is not lucky")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Enter the number of rows in the chocolate bar: "))
m = int(input("Enter the number of columns in the chocolate bar: "))
k = int(input("Enter the number of pieces you want to break the chocolate into: "))

# Check if it's possible to break the chocolate bar into k pieces
if k <= n*m and (k % n == 0 or k % m == 0):
    print("Yes, it's possible to break the chocolate bar into", k, "pieces.")
else:
    print("No, it's not possible to break the chocolate bar into", k, "pieces.")