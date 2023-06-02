import re


global p
global vvod_name
def menu():
    print("Выберите пункт: ")
    print("[1] добавить пользователя в книгу ")
    print("[2] посмотреть всех пользователей ")
    print("[3] удалить пользователя ")
    print("[4] изменить информацию о пользователе ")
    print("[5] найти пользователя ")
    print("[6] завершить работу ")

def check_name():
    i = False
    while not i:  # Цикл будет выполняться пока i не станет True
        name = input('Введите имя: ')
        if re.findall(r'\d',name) == []:  # re.findall(r'\d', name) вернет список из цифр которые используються в значении переменой name, если цифры не использовались вернеться пустой список
            i = True
            return name
        else:
            print("Данные введены неверно, попробуйте еще раз")

def check_number():
    i = False
    while not i:
        number = input('Введите номер: ')
        if re.findall(r'\D',number) == []:  # re.findall(r'\D', name) вернет список из букв которые используються в значении переменой number, если цифры не использовались вернеться пустой список
            i = True
            return number
        else:
            print("Данные введены неверно, попробуйте еще раз")

class book:
    content_book = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        book.content_book[self.name] = self.number

    def add_user(self):
        f = open("Address_book.txt", 'a')  # открываем для записи (writing)
        f.write(self.name + ":" + self.number + "\n")  # записываем текст в файл
        f.close()
        print("Добавлен абонент с именем {} и номером {}".format(self.name, self.number))

    # def view_all(self):
    #     f = open("Address_book.txt", "r")
    #     while True:
    #         line = f.readline()
    #         if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
    #             break
    #         print(line, end='')
    #     f.close()

    def dell(self,ud):
        self.ud = ud
        print("Пользователь удален ".format(book.content_book.pop(self.ud)))
        print("\n")

    def izmenit(self,new_name,new_number):
        self.new_name = new_name
        self.new_number = new_number
        book.content_book[self.new_name] = self.new_number
        print("Номер пользователя {0} изменен с {1} на {2}".format(self.name,self.number, self.new_number))
        print()

    def findal_user(self,names):
        self.names = names
        print("Номер пользователя {0}: {1}".format(self.names,book.content_book.get(self.names)))
        print()

while True:
    menu()
    try:
        vvod = int(input("\nВыберите цифру: "))
        print()
        if vvod > 6:
            print("Число не может быть больше 6, введите число сново\n")
        else:
            pass
    except:
        print("Это не число, введите число\n")
        continue

    if vvod == 1:
        vvod_name = check_name()
        vvod_number = check_number()
        print()
        p = book(vvod_name, vvod_number) # p = book(vvod_name, vvod_number) определение P
        p.add_user()
        print()


    elif vvod == 2:
        f = open("Address_book.txt", "r")
        while True:
            line = f.readline()
            if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
                break
            print(line, end='')
        f.close()
        print()

    elif vvod == 3:
        if (len(book.content_book) == 0):
            print("Адресная книга пуста, сначала заполните ее в пункте [1]\n")
        else:
            print("Введите имя пользователя, которого надо удалить: ")
            udalit = check_name()
            if udalit in book.content_book.keys():
                p.dell(udalit)
            else:
                print("Такого пользователя не существует!\nВведите существующего пользователя: ")
                udalit = check_name()

    elif vvod == 4:
        if (len(book.content_book) == 0):
            print("Адресная книга пуста, сначала заполните ее в пункте [1]\n")
        else:
            print("Введите имя пользователя, номер которого надо изменить: ")
            izmena_name = check_name()
            print(("Введите новый номер: "))
            izmena_number = check_number()
            p.izmenit(izmena_name,izmena_number)


    elif vvod == 5:
        if (len(book.content_book) == 0):
            print("Адресная книга пуста, сначала заполните ее в пункте [1]\n")
        else:
            print("Введите имя пользователя/ей номера, которых нужно найти: ")
            find_us = check_name()
            try:
                p.findal_user(find_us)
            except NameError:
                print("Адресная книга пуста, сначала заполните ее в пункте [1]\n")

    elif vvod == 6:
        print("Программа завершена")
        break
