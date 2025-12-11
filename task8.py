#Задание 1
my_dict = {1: '0101101', 2: '101110', 3: '1A14C', 4: '1100100', 5: '101010'}
print(" Исходный словарь:")
print(my_dict)
if 3 in my_dict:
    my_dict.pop(3)
print(" Словарь после удаления ключа 3:")
print(my_dict)

my_dict[10] = '0100101'
print("Словарь после добавления ключа 10:")
print(my_dict)
#Задание 2
sl = {'</>':13, 'script':1, '__init__':10, 'self':5, 'number_9':6, '#comment':100}
print(" Исходный словарь:")
print(sl)
print(" Добавление нового элемента:")
key_input = input("key: ")
value_input = input("value: ")
sl[key_input] = value_input
print(" Обновленный словарь:")
print(sl)
#Задание 3
my_dict = {}
while len(my_dict) < 3:
    try:
        key_input = int(input("Введите ключ (число): "))
    except ValueError:
        print("Ключ должен быть числом. Попробуйте снова.")
        continue
    
    value_input = input("Введите значение: ")
    my_dict[key_input] = value_input
print("Полученный словарь:")
print(my_dict)
#Задание 4
all_d = {1:15, 4:80, 44:0, 256:15, 100:70, 101:70, 20:44, 3:9}
keys_to_remove = [1, 101, 3]
for key in keys_to_remove:
    if key in all_d:
        del all_d[key]
print(all_d)
