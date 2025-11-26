number = int(input("Введите целое число: "))
if number < 0:
    number = abs(number)
    print(number)
elif number == 0:
    number = 1
    print(number)
else:
    print(number)
#Задание 2
text = input("Введите произвольную строку: ")
if '.' in text or ',' in text:
    print(True)
else:
    print(False)
  #Задание 3
  num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
divisible1 = num1 % 3 == 0
divisible2 = num2 % 3 == 0
if divisible1 and divisible2:
    print(True)
elif divisible1 or divisible2:
    print("Одно число делится на 3")
else:
    print(False)
