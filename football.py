'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''

n = int(input())
matches = [input() for i in range(n)]
#print(matches)


def result(match):
    if int(match[1]) > int(match[3]):
        team1 = [1, 1, 0, 0, 3]
        team2 = [1, 0, 0, 1, 0]
    elif int(match[1]) < int(match[3]):
        team1 = [1, 0, 0, 1, 0]
        team2 = [1, 1, 0, 0, 3]
    else:
        team1 = [1, 0, 1, 0, 1]
        team2 = [1, 0, 1, 0, 1]
    return {match[0]: team1}, {match[2]: team2}


teams_lst = []
for match in matches:
    split_match = match.split(';')
#    print(split_match)
    teams_lst += result(split_match)

#print(teams_lst)

teams_dict = {}
for dict in teams_lst:
    for key, value in dict.items():
        if key not in teams_dict:
            teams_dict[key] = dict[key]
        else:
            for i in range(len(value)):
                teams_dict[key][i] += dict[key][i]

#print(teams_dict)

for key, value in teams_dict.items():
    print(key + ":", *value)


# альтернативное решение
# def command(c, res):
#     if not c in dct: dct[c] = [0, 0, 0, 0, 0]
#     dct[c] = [dct[c][0] + 1,
#                 dct[c][1] + 1 if res == 3 else dct[c][1],
#                 dct[c][2] + 1 if res == 1 else dct[c][2],
#                 dct[c][3] + 1 if res == 0 else dct[c][3],
#                 dct[c][4] + res,]
# dct = {}
# for i in range(int(input())):
#     c1, g1, c2, g2 = input().split(';')
#     command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
#     command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
# for c in dct:
#     print('{}:{} {} {} {} {}'.format(c, *dct[c]))