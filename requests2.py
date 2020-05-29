'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests

f_in = open('dataset_3378_3.txt', 'r')
url = f_in.readline().strip()
f_in.close()

print(url)

r = requests.get(url)
print(r.text)

count = 0
while r.text[0:2] != "We":
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
    print(r.text)
    count += 1
    print(count)

with open('data_out4.txt', 'w') as f_out:
    f_out.write(r.text)

