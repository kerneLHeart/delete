import re

global p
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
        name = input('Введите имя ')
        if re.findall(r'\d',name) == []:  # re.findall(r'\d', name) вернет список из цифр которые используються в значении переменой name, если цифры не использовались вернеться пустой список
            i = True
            return name
        else:
            print("Данные введены неверно, попробуйте еще раз")

def check_number():
    i = False
    while not i:
        number = input('Введите номер ')
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
        print("Добавлен абонент с именем {} и номером {}".format(self.name, self.number))

    def view_all(self):
        print("Вся информация адресной книги: \n", book.content_book.items())
        print("\n")

    def dell(self,ud):
        self.ud = ud
        print("Пользователь {0} удален ".format(book.content_book.pop(self.ud)))
        print("\n")

while True:
    menu()
    try:
        vvod = int(input("\n Выберите цифру: "))
        print()
        if vvod > 6:
            print("Число не может быть больше 6, введите число сново")
        else:
            pass
    except:
        print("Это не число, введите число")

    if vvod == 1:
        vvod_name = check_name()
        vvod_number = check_number()
        print()
        p = book(vvod_name, vvod_number)
        p.add_user()
        print()


    elif vvod == 2:
       try:
           p.view_all()
       except NameError:
           print("Адресная книга пуста, сначала заполните ее в пункте [1]\n")

    elif vvod == 3:
        udalit = input("Введите имя пользователя которого надо удалить: ")
        try:
            p.dell(udalit)
        except NameError:
            print("Адресная книга пуста, сначала заполните ее в пункте [1]\n")

    elif vvod == 4:









#to do
# 1) Одному ключу соответствует несколько значений
# 2) Одинаковые переменные ключ:значение

#p = book(vvod_name,vvod_number)
#p.add_user()
#p.view_all()