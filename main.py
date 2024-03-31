import random

words = ['питон', 'компьютер', 'коала', 'артист', 'калькулятор', 'обезьяна']

while True:
    command = input("Введите команду\n").lower()
    if command == 'выйти':
        exit()
    elif command == 'играть':
        word = random.choice(words)
        print(f"Длина слова - {len(word)}")
        choice = input("Сделайте ход\n")
        while len(choice) != len(word):
            print("Вы ввели слово неверной длины")
            choice = input("Сделайте ход\n")
        while choice != word:
            bull = 0
            cow = 0
            for i in range(len(choice)):
                if choice[i] in word:
                    if choice[i] == word[i]:
                        bull += 1
                    else:
                        cow += 1
            print(f"У вас {bull} быков и {cow} коров")
            choice = input("Сделайте ход\n")
        print(f"Поздравляем! Вы угадали слово {word}")
    else:
        print("Неверная команда.")
