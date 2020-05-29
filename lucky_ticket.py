'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет,
счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр совпадает
с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают,
и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''


n = str(input())

if (int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5])):
    print("Счастливый")
else:
    print("Обычный")