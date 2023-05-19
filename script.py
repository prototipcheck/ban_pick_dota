#импортируем библы
import pandas as pd
from random import randint

#импортируем DF с героями доты
heroes = pd.read_csv("./heroes.csv")

pick = {'heroes': ['pudge','crystal_maiden', 'windrunner', 'nevermore', 'jakiro', 'lina', 'drow_ranger', 'sniper','obsidian_destroyer']}
rus_pick =['пудж', 'девочка-цмочка', 'вр', 'сф', 'джакиро', 'лина', 'дровка', 'снайпер', 'од']
pickedHeroes = pd.DataFrame(pick)
idHeroes = pickedHeroes.merge(heroes, how='inner', left_on = 'heroes', right_on='name')
idHeroes.drop(labels='name', axis=1)
idHeroes = idHeroes[['id', 'localized_name', 'heroes']]
idHeroes['heroes_in_rus'] = rus_pick


#пишем ники
print('='*50)


print('Welcome to the club, buddy!')

while True:

    confirm = 'f'

    while True:

        if confirm != 'y':

            first_nic = input("Write first nickname")

            second_nic = input("Write second nickname")

            confirm = input('It is your nicknames?)\nIf you want to start write "y", else - write something another')

        if confirm == 'y':

            print(f'First nickname is: {first_nic}')

            print(f'Second nickname is: {second_nic}')
            
            print('='*50)

            break    
    break

#выбираем очередь 
print('='*50)
flagRandom = input('OK! Do you want to randomly decide who will be the first to ban/pick? Write "y" to Yes, else - write something another')
if flagRandom == 'y':
    turn = randint(1,2)

    if turn == 1:
        print(f'{first_nic} may start pick')
        first_turn = first_nic
        second_turn = second_nic
    else:
        print(f'{second_nic} may start pick')
        first_turn = second_nic
        second_turn = first_nic
else:
    while True:
        turn = input('Alright, write, who can get start: 1 - if first player, 2 - if second player. Write something another, if you are retarded')
        if turn == '1':
            print(f'{first_nic} may start pick')
            first_turn = first_nic
            second_turn = second_nic
            break
        elif turn == '2':
            print(f'{second_nic} may start pick')
            first_turn = second_nic
            second_turn = first_nic
            break
        else:
            print('You really idiot;(')




# Создаем два списка для выбранных героев каждым игроком
order = ['ban', 'ban', 'pick', 'pick', 'ban', 'ban', 'ban', 'ban', 'desider']
queue = ['first', 'second', 'first', 'second','first', 'second', 'first', 'second', 'desider']
player1_heroes = []
player2_heroes = []
last_columns = ['pick', 'picked_hero', 'player']
final_df = pd.DataFrame(columns=last_columns)

# Проходимся по всем элементам списка порядка банов и пиков


for countval,event in enumerate(order):

    if event == 'ban':
        print('='*50)
        print(idHeroes)
        print('='*50)

        if queue[countval] == 'first':

            banned_hero = input(f"{first_turn} : Please choose a hero to ban: ")

        else:

            banned_hero = input(f"{second_turn} : Please choose a hero to ban: ")

        idHeroes = idHeroes[idHeroes.heroes_in_rus != banned_hero] # Удаляем заблокированный герой из dataframe

        print('='*50)
        print(idHeroes)
        print('='*50)

    elif event == 'pick':

                # Предлагаем игрокам выбрать героя для пика
        if queue[countval] == 'first':

            print('='*50)
            print(idHeroes)
            print('='*50)

            print(f"{first_turn} : It's your pick!")

            picked_hero = input("Please choose a hero: ")

            final_df.loc[countval] = [countval, picked_hero, first_turn]

            print('='*50)
            print(idHeroes)
            print('='*50)

            # player1_heroes.append(picked_hero) # Добавляем выбранный герой в список игрока 1
            
        else:

            print('='*50)
            print(idHeroes)
            print('='*50)

            print(f"{second_turn} : It's your pick!")



            picked_hero = input("Please choose a hero: ")

            final_df.loc[countval] = [countval, picked_hero, second_turn]

            print('='*50)
            print(idHeroes)
            print('='*50)            

            # player2_heroes.append(picked_hero) # Добавляем выбранный герой в список игрока 2

        idHeroes = idHeroes[idHeroes.heroes_in_rus != picked_hero] # Удаляем выбранный герой из dataframe
                
                
    elif event == 'desider':

            # Предлагаем игрокам выбрать героя для десайдера

        print("Desider pick!")

        print(idHeroes)

        picked_hero = input("Please choose a hero: ")

        final_df.loc[countval] = [countval, picked_hero, 'Desider']

        desider_hero = picked_hero # Присваиваем выбранного героя десайдеру
            
        break

        

print(final_df)
