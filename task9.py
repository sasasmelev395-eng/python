notebook = {}

def add_note():
    key = input("Введите название заметки: ")
    value = input("Введите содержимое заметки: ")
    notebook[key] = value
    print("Заметка добавлена")

def read_notes():
    if notebook == False:
        print("Заметок нет")
    else:
        for key in notebook:
            print(key)
        note_name = input("Ввдеите название заметки для чтения: ")
        if note_name in notebook:
            print("\nЗамтка:")
            print(notebook[note_name])
        else:
            print("Такой заметки нет")
while True:
    print("\n1 - Создать заметку\n2 - Прочитать заметку\n3 - Выйти")
    choice = input ("Выберите действие: ")
    if choice == '1':
        add_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        print("Программа отключена")
        break
    else:
        print("Неверная команда")
