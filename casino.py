import random

def game():
    diff_list = []
    players_list = []
    player_count = int(input("Введите количество игроков: "))
    while player_count < 0 or player_count > 4:
        print("Неверное количество игроков")
        player_count = int(input("Введите количество игроков: "))
    rnum = random.randint(2,21)
    print("rnum = ", rnum)

    for i in range(player_count):
        num = int(input("Введите число от 2 до 21: "))
        players_list.append(num)
    for j in range(len(players_list)):
        print(f"Игрок {j+1} назвал число", players_list[j])
        difference = abs(rnum-players_list[j])
        diff_list.append(difference)
    min = diff_list[0]
    print(diff_list)
    for i in range(len(diff_list)):
        if min > diff_list[i]:
            min = diff_list[i]
            remember = i

    print(f"Игрок {remember+1} назвал число", players_list[remember], "с разницей в ", min,"и победил")
game()