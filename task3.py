# Задание 1
min = int(input("введите минуты"))
hours = min // 60
hours_min = min % 60
print(f">>> {hours}")
print(f">>> {hours_min}")
#Задание 2
a = 8
b = 10
h = 7
if a <= h <= b:
    print("Норм")
elif h < a:
    print("недосып")
else:
    print("пересып")
 #Задание 3
import math
a = int(input("Введите длину стороны а"))
b = int(input("Введите длину стороны б"))
c = int(input("Введите длину стороны с"))
p = (a + b + c) / 2
S = math.sqrt(p*(p-a) * (p-b) * (p-c))
print(f"Площадь треугольника:{S}")
#Задание 4
figure = input()
if figure == "Треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c ) / 2
    S = (p*(p-a) * (p-b) * (p-c)) ** 0.5
elif figure == "Прямоугольник":
    a = int(input())
    b = int(input())
    S = a*b
elif figure == "Круг":
    r = int(input())
    S = 3.14 * r * r
print(S)
#Задание 5
n = int(input("Введите число"))
last_digit = n % 10
last_two_digits = n % 100 
if 11 <= last_two_digits <= 14:
    print(f"{n} программист")
else:
    if last_digit == 1:
        print(f"{n} программист")
    elif 2 <= last_digit <=4:
        print(f"{n} программист")
    else:
        print(f"{n} программист")
#Задание 6
ticket = input()
if len(ticket) != 6:
    print("Неверный номер билета")
else:
    first_half = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second_half = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if first_half == second_half:
    print("Счастливый")
else:
    print("Несчастливый") 
