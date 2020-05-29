'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны
символы исходного алфавита, на второй строке — символы конечного алфавита, после
чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:
*d*%*d*#*d*
dacabac
'''


s = input()
code = input()

s_to_encode = input()
s_to_decode = input()

d = dict(zip(s, code))
#print(d)

s_encoded = ''
s_decoded = ''

for i in range(len(s_to_encode)):
    for key, value in d.items():
        if s_to_encode[i] == key:
            s_encoded += value

for i in range(len(s_to_decode)):
    for key, value in d.items():
        if s_to_decode[i] == value:
            s_decoded += key

print(s_encoded)
print(s_decoded)



# короткое решение
# a,b,c,d=input(),input(),input(),input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))