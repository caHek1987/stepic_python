'''
На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия
"Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того,
чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу,
используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится,
надо отправить в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
'''

with open('dataset_3363_2.txt') as inf:
    s = inf.readline().strip()

print(s)
s_new = ''
sum = ''
step = 1
for i in range(len(s)):
    if s[i] < 'A':
        sum += s[i]
        if i == len(s)-1:
            num = int(sum)
            s_new += s[i-step] * num
        step += 1

    else:
        if sum == '':
            num = 0
        else:
            num = int(sum)
            s_new += s[i-step] * num
            sum = ''
            step = 1

print(s_new)

with open('data_out.txt', 'w') as ouf:
    ouf.write(s_new)


# with open('dataset_3363_2.txt') as dataset:
#     inf = dataset.readline()
#
# numbers = "0123456789"
# count = ''
# bukva = inf[0]
# result = ''
#
# for i in inf:
#     if i in numbers:
#         count += i
#     elif i != bukva:
#         result = result + bukva * int(count)
#         bukva = i
#         count = ''
#
# with open('file.txt', 'w') as res:
#     res.write(result)