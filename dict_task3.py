'''
Напишите программу, которая считывает строку с числом n,
которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x_i, по одному числу в каждой строке.
Итого будет n+1 строк.
При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i).
Функция f(x) уже реализована и доступна для вызова.
Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:
5
5
12
9
20
12
Sample Output:
11
41
47
61
41
'''

def f(x):
    return 2 * x

n = int(input())
dict = {}
lst = []
for i in range(n):
    x_i = int(input())
    lst.append(x_i)
    if x_i not in dict:
        dict[x_i] = f(x_i)
for l in lst:
    print(dict[x_i])

'''
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}    # преобразовали список а в множество и тем самым исключили повторения
for i in a:
    print(b[i])
'''