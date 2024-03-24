'''
Создается список из 10 чисел и заполняется случайными числами в диапазоне от 1 до 10.
Элементы этого списка необходимо записать в файл в одну строку.
Необходимо выполниь  15 раз функцию choicce из этого списка и
сохранить этот элемент внутрь второго списка
вывести на консоль элементы второго списка.
'''
import random


def task1():
    list1 = list()
    list2 = list()
    temp = 0
    for i in range(10):
        num1 = random.randrange(1, 10)
        list1.append(num1)
    print(list1)
    with open("test.txt", "w") as test_file:
        for i in list1:
            test_file.write(str(i))
    while temp < 15:
        elem = random.choice(list1)
        list2.append(elem)
        temp += 1
    print(list2)


# task1()
'''
заполнить список из 10 элементов числами с клавиатуры
создать еще один список, в котором будет 10 элементов, 
каждый из элементов генерируется случайным образом в диапазоне от 0 до 10
необхоимо проверить относителньо второго списка, если элемент больше 5, 
посчитать произведение первого элемента из первого списка на первый элемент из второго списка
если элемент меньше 5 посчитать их сумму, каждый результат добавить в список. 
Вывести на печать итоговый список
'''


def task2():
    list1 = list()
    list2 = list()
    list3 = list()
    for i in range(10):
        num = int(input("Введите число"))
        list1.append(num)
    print(list1)
    for i in range(10):
        num = random.randrange(0, 10)
        list2.append(num)
    print(list2)
    j = 0
    for i in list2:
        if i > 5:
            result = list1[j] * list2[j]
            list3.append(result)
        elif i < 5:
            result = list1[j] + list2[j]
            list3.append(result)
        j += 1
    print(list3)


# task2()
'''
При запуске программы высвечивается сообщение
если выбирается
1. то необходимо выбрать далее: посчитать площадь круга/площадь прямоугольника/площадь треугольника
 или математическую операцию из двух чисел
2. то считываем с консоли текст и записываем его внутрь файла
3. считываем информацию из файла
4. если введено что то помимо 1,2,3 то выовдится сообщение некорректная операция и 
просит ввести число еще ращ
'''


def task3():
    print("1. Посчитать")
    print("2. Записать")
    print("3. Почитать")
    operation = int(input("Выберите операцию: "))
    if operation == 1:
        print("1. Посчитать площадь круга")
        print("2. Посчитать площадь прямоугольника")
        print("3. Посчитать площадь треугольника")
        print("4. Посчитать математическую операцию")
        new_operation = int(input("Выберите операцию: "))
        if new_operation == 1:
            r = int(input("Введите радиус: "))
            s = 3.14 * r ** 2
            print(s)
        elif new_operation == 2:
            a = int(input("Введите первую сторону: "))
            b = int(input("Введите вторую сторону: "))
            s = a * b
            print(s)
        elif new_operation == 3:
            a = int(input("Введите  сторону: "))
            h = int(input("Введите  высоту: "))
            s = a * h / 2
            print(s)
        elif new_operation == 4:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(a, "+", b, " = ", a + b)
            print(a, "-", b, " = ", a - b)
            print(a, "*", b, " = ", a * b)
            print(a, "/", b, " = ", a / b)
        else:
            print("Некоректная операция")
    elif operation == 2:
        str1 = (input("Введите текст: "))
        with open("text.txt", "w") as text_file:
            text_file.write(str1)
    elif operation == 3:
        with open("text.txt", "r") as text_file:
            str = text_file.readlines()
            print(str)
    else:
        print("Некорректная операция")


# task3()

'''
Считываем целые числа из файла numbers.txt
все четные числа, записываем в новый файл new_numbers.txt
'''


def task4():
    new_list = list()
    with open("numbers.txt", "r") as file1:
        for line in file1:
            if int(line) % 2 == 0:
                new_list.append(line)
        print(new_list)
    with open("new_numbers.txt", "w") as file2:
        for i in new_list:
            file2.write(str(i))


# task4()
'''
Напишите программу, которая будет предлагать пользователю 
ввести названия любимых фильмов. После ввода всех названий фильмов,
 программа сохранит их в файл "favorite_movies.txt" 
 и выведет список всех введенных фильмов на экран.
'''


def task5():
    movies = list()
    while True:
        movie = input("Введите название фильма: ")
        print("Чтобы закончить ввод введите 'stop' ")
        if movie.lower() == 'stop':
            break
        else:
            movies.append(movie)

    with open("favourite_movies.txt", "w") as movies_file:
        for movie in movies:
            movies_file.write(movie + "\n")
    for movie in movies:
        print(movie)


# task5()


'''
Эта программа позволяет пользователю управлять списком задач, 
сохранять его в файл "tasks.txt", 
просматривать, отмечать как выполненные и удалять задачи. 
Пользователь может продолжать взаимодействие с программой или 
завершить её, выбрав соответствующий пункт меню.
'''


def task6():
    def create_task_list():
        tasks = []
        while True:
            task = input("Введите новую задачу или "
                         "нажмите Enter для завершения: ")
            if task == "":
                break
            tasks.append(task)

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

    def view_task_list():
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                print(task.strip())

    def mark_task_done():
        tasks = []
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        print("Список задач:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")

        task_num = int(input("Введите номер задачи для "
                             "отметки выполненной: "))
        tasks[task_num - 1] = (tasks[task_num - 1].strip() +
                               " - выполнено\n")

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task)

    def delete_task():
        tasks = []
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        print("Список задач:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")

        task_num = int(input("Введите номер задачи для удаления: "))
        del tasks[task_num - 1]

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task)

    while True:
        print("Выберите действие:")
        print("1. Добавить новую задачу")
        print("2. Просмотреть список задач")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            create_task_list()
        elif choice == "2":
            view_task_list()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


# task6()


'''
сгенерировать два случайных числа от 1 до 100
создать список из 7 элемментов заполненный числами из диапазона
от первого числа до второго
Проверяем, если число четное, записываем в файл even.txt
иначе записываем в файл notEven.txt
'''


def task8():
    spisok = list()
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    for i in range(7):
        spisok.append(random.randint(r1, r2))
    print(spisok)
    for i in spisok:
        if i % 2 == 0:
            with open("even.txt", "a") as file:
                file.write(str(i) + "\n")
        else:
            with open("notEven.txt", "a") as file:
                file.write(str(i) + "\n")


# task8()

'''
На вход поступает число, 
если оно четное, то добавляем в список четных числе,
иначе добавляем в список нечетных чисел
Числа вводятся до тех пор, пока не будет введено число 0

Пройтись по четному списку и проверить, 
если число делится  на 4 или на 6
то добавить в file1.txt
иначе добавить в file2.txt

Пройтись по нечетному списку, проверить
если число делится на 3 или на 5, то добавить в file1.txt
иначе добавить в file2.txt

'''


def task9():
    with open("file1.txt", "w") as file1:
        pass
    with open("file2.txt", "w") as file2:
        pass
    even_list = list()
    not_even_list = list()
    while True:
        number = int(input("Введите число: "))
        if number == 0:
            break
        if number % 2 == 0:
            even_list.append(number)
        else:
            not_even_list.append(number)
    print(even_list)
    print(not_even_list)
    for i in even_list:
        if i % 4 == 0 or i % 6 == 0:
            with open("file1.txt", "a") as file1:
                file1.write(str(i) + "\n")
        else:
            with open("file2.txt", "a") as file2:
                file2.write(str(i) + "\n")
    for i in not_even_list:
        if i % 3 == 0 or i % 5 == 0:
            with open("file1.txt", "a") as file1:
                file1.write(str(i) + "\n")
        else:
            with open("file2.txt", "a") as file2:
                file2.write(str(i) + "\n")


# task9()
'''
Заполнить список случайными числами в диапазоне от 0 до 100
количество элементов в списке будет случайным, от 10 до 20
посчитать суммы всех нечетных индексов и четных индексов в списке
'''


def task10():
    list1 = list()
    rnum = random.randint(10, 20)
    for i in range(rnum):
        list1.append(random.randint(0, 100))
    print(list1)
    list1.sort()
    print(list1)
    index = len(list1)
    sum1 = sum(list1[1::2])
    sum2 = sum(list1[0::2])
    print(sum1)
    print(sum2)
    i = 0
    sum3 = 0
    sum4 = 0
    while i < index:
        if i % 2 == 0:
            sum3 = sum3 + list1[i]
        else:
            sum4 = sum4 + list1[i]
        i += 1
    print(sum1)
    print(sum2)


# task10()

'''
создать два файла, в каждый из них записать информацию с консоли
Первый файл содержит название товара, product.txt
Второй файл содержит стоимость товара price.txt
Вывести на печать информациб об объекте в целом
'''


def task11():
    products = list()
    prices = list()
    with open("product.txt", "w") as file1:
        while True:
            product = str(input("Введите название товара"))
            file1.write(product)
            file1.write("\n")
            products.append(product)
            if product == '':
                break
    with open("price.txt", "w") as file2:
        for i in range(len(products) - 1):
            print("Введите стоимость товара", " ", products[i])
            price = input()
            file2.write(str(price))
            file2.write("\n")
            prices.append(price)

    for i in range(len(products) -1):
        print(products[i],"цена:",prices[i],"рублей")
#task11()
'''
Заполнить словарь элементами с клавиатуры, 
количество элементов случайное - от 5 до 10
каждый элемент должен иметь случайный ключ от 0 до 20
значение задается с консоли
вывести словарь на печать
'''
def task12():
    dict1 = {}
    rnum = random.randint(5,10)
    print("Количество элементов", rnum)
    for i in range (rnum):
        key = random.randint(0,20)
        value = input("Введите значения")
        print(key,value)
        dict1[key] = value
    print(dict1)
#task12()

'''
заполнить словарь из 7 элементов значениями с клавиатуры
значения должны быть целыми числами
если сумма нечентеных значений больше суммы четных значений 
то записываем результат суммы внутрь кортежа
иначе записываем элементы внутрь списка
вывести этот кортеж
'''
def task13():
    dict = {}
    list = []
    tuple = ()
    sum1 = 0
    sum2 = 0
    for i in range(7):
        key = input("Введите ключ ")
        value = int(input("Введите значение"))
        dict[key] = value
        if value %2 ==0:
            sum1 +=value
        else:
            sum2+=value
    if sum2 > sum1:
        list.append(sum1)
        list.append(sum2)
        tuple = tuple(list)
        list.clear()
    else:
        for value in dict.items():
            list.append(value)
    print("Список: ",list)
    print("Кортеж: ", tuple)
    print("Словарь ",dict)


#task13()

'''
Заполнить множество случайными числами в диапазоне от 0 до 100
количество этих элементов вводится с консоли
после этого записать элементы полученного множества 
в отсортированном формате внутрь файла numbers.txt
'''
def task14():
    set1 = set()
    count = int(input("введите количество чисел: "))
    for i in range (count):
        rnum = random.randint(0,100)
        set1.add(rnum)
    print(set1)
    with open("numbers.txt", "w") as file:
        for i in set1:
            file.write(str(i) + "\n")
task14()
