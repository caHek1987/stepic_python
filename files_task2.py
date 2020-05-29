'''
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''

f_in = open('dataset_3363_3.txt', 'r')
words = f_in.read().lower().strip().split()
f_in.close

print(words)

sorted_words = sorted(words)
print(sorted_words)

dict = {}
for word in sorted_words:
    dict[word] = sorted_words.count(word)
print(dict)

def get_first_max_key(d):
    for key, value in d.items():
        if value == max(d.values()):
            return key, value

answer = get_first_max_key(dict)
s = str(answer[0]) + " " + str(answer[1])
print(s)

f_out = open('data_out2.txt', 'w')
f_out.write(s)
f_out.close


# with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
#     maxc = 0
#     s = inf.read().lower().strip().split()
#     s.sort()
#     for word in s:
#         counter = s.count(word)
#         if counter > maxc:
#             maxc = counter
#             result_word = word
#     ouf.write(result_word +' ' + str(maxc))