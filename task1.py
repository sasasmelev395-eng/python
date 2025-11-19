#Задание 1 
first_num = 9
second_num = 7.8
my_str  = "start"
print(first_num,second_num,my_str)
first_num1 = 5.2
print(first_num1, type(first_num1))
third_num = first_num1 + second_num
print(third_num, type(third_num))
first_num1 += 5
second_num += first_num1
print(first_num1, second_num)
second_num1 = int(second_num)
print(first_num1, second_num1)
my_str += "&stop"
print(my_str)
print(my_str * 5)
#Задание 2
path = "C:\\Users\\MainAdmin\\Desktop\\programs"
print(path)
path += "'\\game.exe"
print(path)
path = "C:\\Users\\MainAdmin\\Desktop\\files"
path += "\\picture.png"
print(path)
path = "C:\\Games\\city simulator"
path *= 2
print("Error path:", path )
# задание 3
num1 = 7
num2 = 10
num3 = 4
summ = num1 + num2 + num3
print(f"Сумма всех чисел:{summ}")
num1 = 7.9
num2 = 21.3
num_3 = float(num3)
summ = num1 + num2 + num3
print(f"Сумма всех чисел:{summ}")
num1 = 130
num2 = 4
num3 = 2
multiplying = num1 * num2 * num3
print(f"Произведение всех чисел:{multiplying}")
num4 = num1 / num2
division = num4 / num3
print(f"Деление: {division}")
num1 = 2
num2 = 3
num3 = 4
degree = num1 ** num2 ** num3
print(f"Числа в степени {degree}")
num1 = 2
num2 = 8
num3 = 5
math = ((43 + num1) + (num2 + 67) - (num3 * 2)) // 2 
print(math)
