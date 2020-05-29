'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов,
а в качестве роста используется натуральное число, но при подсчёте среднего
требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса
(для классов с первого по одиннадцатый). Если про какой-то класс нет информации,
необходимо вывести напротив него прочерк, например:

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

f_in = open('dataset_3380_5.txt', 'r')
students = f_in.readlines()
f_in.close

# n = int(input())
# students = [input() for i in range(n)]

dict = {i: [0, 0] for i in range(1, 12)}
#print(dict)

for student in students:
    split_student = student.split()
#    print(split_student)
    dict[int(split_student[0])][0] += int(split_student[2])
    dict[int(split_student[0])][1] += 1
#    print(dict)

for key, value in dict.items():
    if value[1] == 0:
        dict[key] = '-'
    else:
        dict[key] = value[0] / value[1]
print(dict)

f_out = open('data_out5.txt', 'w')
for key, value in dict.items():
    f_out.writelines(str(key) + ' ' + str(value) + '\n')
f_out.close


