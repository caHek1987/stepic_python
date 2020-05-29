'''
На вход программе первой строкой передаётся количество d известных нам слов,
после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
'''


n_words = int(input())
words_list = [input().lower() for i in range(n_words)]

n_strings = int(input())
strings = [input().lower() for i in range(n_strings)]

print(n_words, words_list)
print(n_strings, strings)

errors = set()
for string in strings:
    split_string = string.split()
    print(split_string)
    for word in split_string:
        if word not in words_list:
            errors.add(word)
            print(word, errors)
for error in errors:
    print(error)

