import random

'''
Создайте программу на Python, которая будет принимать на вход символы (например, 'A', 'B', 'C')
и выводить их ASCII значения, а также наоборот - принимать на вход ASCII значения и выводить соответствующие символы.
Затем программа должна запросить пользователя ввести несколько символов или ASCII значений и вывести соответствующие
значения/символы.
'''


def task1():
    def char_to_ascii(s):
        result = [ord(c) for c in s]
        return result

    def ascii_to_char(nums):
        result = [chr(n) for n in nums]
        return ''.join(result)

    input_type = input("Выберите тип ввода (1 - символ, 2 - ASCII): ")

    if input_type == '1':
        symbol = input("Введите символ: ")
        print("ASCII значение:", char_to_ascii(symbol))
    elif input_type == '2':
        numbers = input("Введите ASCII значение через пробел: ")
        nums_list = [int(num) for num in numbers.split()]
        print("Символ:", ascii_to_char(nums_list))
    else:
        print("Ошибка: выбран неверный тип ввода.")


#task1()


def task2():
    import random

    def write_to_file():
        words = input("Введите слова через пробел, которые хотите записать в файл: ")
        with open("words.txt", "a",encoding="utf8") as file:
            file.write(words)

    def read_from_file():
        with open("words.txt", "r",encoding="utf8") as file:
            words = file.read().split()
        return random.choice(words)

    def play_game():
        word = read_from_file()
        guessed_letters = set()
        attempts = 3
        while attempts > 0:
            print("Угадайте слово:")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print()
            guess = input("Введите букву: ")
            if guess in word:
                guessed_letters.add(guess)
            else:
                attempts -= 1
            if guessed_letters == set(word):
                print("Поздравляю, вы угадали слово!")
                break
        if attempts == 0:
            print(f"Вы не угадали слово. Загаданное слово было: {word}")

    a = int(input("Введите номер"))
    if a == 1:
        write_to_file()
    elif a == 2:
        play_game()
    else:
        print("Ошибка")
#task2()

def task3():
    def add_user_to_file(name, age, email):
        with open('users.txt', 'a',encoding="utf8") as file:
            file.write(f'{name},{age},{email}\n')

    def search_user_in_file(name):
        with open('users.txt', 'r',encoding="utf8") as file:
            for line in file:
                user_data = line.split(',')
                if user_data[0] == name:
                    return f'Name: {user_data[0]}, Age: {user_data[1]}, Email: {user_data[2]}'
            return 'User not found'

    # Заполнение данных о пользователе с консоли
    name = input('Введите имя пользователя: ')
    age = input('Введите возраст пользователя: ')
    email = input('Введите email пользователя: ')
    add_user_to_file(name, age, email)

    # Поиск пользователя
    search_name = input('Введите имя пользователя, информацию о котором вы хотите найти: ')
    print(search_user_in_file(search_name))
#task3()

def task4():
    import os

    def get_words(filename):
        with open(filename, encoding="utf8") as file:
            text = file.read()
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
        text = text.lower()
        words = text.split()
        words.sort()
        return words

    def get_words_dict(words):
        words_dict = dict()

        for word in words:
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1
        return words_dict

    def main():
        filename = input("Введите путь к файлу: ")
        if not os.path.exists(filename):
            print("Указанный файл не существует")
        else:
            words = get_words(filename)
            words_dict = get_words_dict(words)
            print(f"Кол-во слов: {len(words)}")
            print(f"Кол-во уникальных слов: {len(words_dict)}")
            print("Все использованные слова:")
            for word in words_dict:
                print(word.ljust(20), words_dict[word])
    main()
task4()