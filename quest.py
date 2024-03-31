print('Я медленно открываю глаза')
print('Голова просто раскалывается')
print('Что произошло? Где я нахожусь?')
print('Сырость и мрак. Похоже на какую-то пещеру')
print('Надо отсюда выбираться...')
current_room = "Пещера"
end_of_game = False
key = False
mine = False
blockage = True

'''while not end_of_game:
    if current_room == 'Пещера':
        print('Я зашёл в пещеру')
        if blockage:
            print("Здесь два прохода, но один завален камнями")
        else:
            print("У меня есть два пути, куда пойти?")
        print('1. Перейти в шахту')
        if blockage:
            if mine:
                print('2. Уничтожить завал киркой')
            else:
                print('2. Разобрать завал')
        else:
            print('2. Перейти в кладовую')
        print('Выберите действие')
        where = int(input())
        while where != 1 and where != 2:
            print('Некорректный вариант. Выберите действие')
            where = int(input())
        if where == 1:
            current_room = "Шахта"
        elif blockage and mine:
            print('Мне удалось уничтожить завал киркой')
            blockage = False
        elif blockage and not mine:
            print('Завал слишком большой, не получается разобрать его руками')
            print('Нужно найти инструмент')
        else:
            current_room = "Кладовая"

    elif current_room == 'Шахта':
        print('Я зашёл в шахту')
        print('Осмотревшись вокруг, я нашёл какой-то проход и сундук')
        print('1. Перейти в пещеру')
        print('2. Перейти в тронный зал')
        print('3. Открыть сундук')
        where = int(input())
        while where != 1 and where != 2 and where != 3:
            print('Некорректный вариант. Выберите действие')
            where = int(input())
        if where == 1:
            current_room = "Пещера"
        elif where == 2:
            current_room = "Зал"
        else:
            if not mine:
                print("Я нашёл в сундуке кирку")
                mine = True
            else:
                print("Сундук пуст")
    elif current_room == 'Кладовая':'''



