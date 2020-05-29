'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и
для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке,
соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике,
физике и русскому языку по всем абитуриентам.
В качестве ответа на задание прикрепите полученный файл со средними оценками.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''


f_in = open('dataset_3363_4.txt', 'r')
students = f_in.read().strip().split('\n')
f_in.close

print(students)

sum_math = 0
sum_phys = 0
sum_lang = 0
averages = []
for student in students:
    s = student.split(';')
    print(s)
    average = (int(s[1]) + int(s[2]) + int(s[3])) / 3
    print(s[0], average)
    averages.append(str(average))
    sum_math += int(s[1])
    sum_phys += int(s[2])
    sum_lang += int(s[3])

print(averages)

average_math = str(sum_math / len(students))
average_phys = str(sum_phys / len(students))
average_lang = str(sum_lang / len(students))
print(average_math, average_phys, average_lang)

with open('data_out3.txt', 'w') as f_out:
    for average in averages:
        f_out.write(average + '\n')
    f_out.write(average_math + " " + average_phys + " " + average_lang)





