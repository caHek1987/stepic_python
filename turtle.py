'''
Программе подаётся на вход число команд n, которые нужно выполнить черепашке,
после чего n строк с самими командами. Вывести нужно два числа в одну строку:
первую и вторую координату конечной точки черепашки. Все координаты целочисленные.
Для простоты считать, что движение начинается в точке (0, 0),
и движение на восток увеличивает первую координату, а на север — вторую.

Sample Input:
4
север 10
запад 20
юг 30
восток 40

Sample Output:
20 -20
'''

x, y = 0, 0

n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == 'север':
        y += int(command[1])
    elif command[0] == 'юг':
        y -= int(command[1])
    elif command[0] == 'восток':
        x += int(command[1])
    elif command[0] == 'запад':
        x -= int(command[1])

print(x, y)


# n=int(input())
# d={'север':0,'запад':0,'юг':0,'восток':0}
# for i in range(n):
#     x=input().split()
#     d[x[0]]+=int(x[1])
# print(d['восток']-d['запад'], d['север']-d['юг'])



