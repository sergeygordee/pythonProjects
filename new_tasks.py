import random


def task1():
    list1 = []
    list2 = []
    num1 = random.randint(1, 20)
    list1.append(num1)
    for i in range(5):
        num2 = random.randint(1, 20)
        list1.append(num2)
    for i in list1:
        if i % 3 == 0:
            list2.append(i)
    print(list1)
    print(list2)


# task1()

'''
Заполнить файл под названием names.txt именами с клавиатуры,
где каждое имя начинается с закглавной буквы
ввод осуществляется до тех пор, 
пока не будет введено ключевое слово stop
'''


def task2():
    def writeUser():
        with open("names.txt", "w") as new_file:
            while True:
                name = input("Введите имя")
                if name == 'stop':
                    break
                new_file.write(name + '\n')

    def readUsers():
        list1 = []
        with open("names.txt", "r") as new_file:
            list1 = new_file.readlines()
        for i in list1:
            if i[0] != 'A':
                print(i)
    print("Выберите действие")
    print("1. Добавить пользователей")
    print("2. Посмотреть пользователей")
    action = int(input("Введите действие"))
    if action == 1:
        writeUser()
    elif action == 2:
        readUsers()
    else:
        print('error')





task2()
