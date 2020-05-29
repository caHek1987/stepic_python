def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <=2:
        return -x / 2
    else:
        return (x - 2) ** 2 + 1

#print(f(-4.5))


'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, 
удаляет из него все нечётные значения, а чётные нацело делит на два. 
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.
'''

def modify_list(l):
    for n in l[::-1]:
        if n%2 == 1:
            l.remove(n)
    for i in range(len(l)):
        l[i] = l[i] // 2

#    l[:] = [i // 2 for i in l if i % 2 == 0]

lst = [1, 3, 5, 7]
print(modify_list(lst))  # None
print(lst)               # []

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]