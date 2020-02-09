# 1. Написати скрипт, який з двох введених чисел визначить, яке з них більше,
# а яке менше.
'''
a = int(input("enter first number:"))
b = int(input("enter sekond number:"))
print(f"number {a} is biger then {b}"if a > b else f"number {b} is biger then {a}")
'''
# 2. Написати скрипт, який перевірить чи введене число парне чи непарне
# і вивести відповідне повідомлення.
'''
number = int(input("Enter pleas number:"))
print("number is even"if number % 2 == 0 else "number is odd")
'''
# 3. Написати скрипт, який обчислить факторіал введеного числа.
'''
number = int(input("Enter pleas number:"))
a = int(number)
while a != 1:
    number = number * (a-1)
    a = a-1
print(number)


chyslo = input('enter factorial :')
t = 1
for i in range(1, int(chyslo)+1):
    t *= i
print(t)
'''
# 1. Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один
# використовуючи цикл while, а інший з використанням циклу for).
'''
a = 1
while a < 100:
    if a % 2 == 0:
        print(a)
    a = a + 1
'''
'''
for i in range(0,101,2):
    print(i)
'''
# 2. Роздрукувати всі непарні числа менші 100. (написати два варіанти коду:
# один використовуючи оператор continue, а інший без цього оператора).
'''
a = 0
while a < 100:
    a = a + 1
    if a % 2 == 0:
        continue
    else:
        print(a)
'''
'''
for i in range(100):
    if i % 2 == 0:
        continue
    else:
        print(i)
'''
'''
a = 0
while a < 100:
    a = a + 1
    if a % 2 == 0:
        pass
    else:
        print(a)
'''
'''
for i in range(100):
    if i % 2 == 0:
        pass
    else:
        print(i)
'''
'''
for i in range(1,100,2):
    print(i)
'''
# 3. Перевірити чи список містить непарні числа.
# (Підказка: використати оператор break)
'''
pass
'''
# 4.  Створити список, який містить елементи цілочисельного типу, потім за
# допомогою циклу перебору змінити тип даних елементів на числа з плаваючою
# крапкою. (Підказка: використати вбудовану функцію float ()).
'''
spysok = list(range(10))
for i in spysok:
    spysok[i] = float(spysok[i])
print(spysok)
'''
# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи
#  цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
'''
pass
'''
# 6.  Створити список, що складається з чотирьох елементів типу string. Потім,
#  за допомогою циклу for, вивести елементи по черзі на екран.
'''
spysok = ["Helow,", "World!", "how're", "you?"]
for i in spysok:
    print(i)
'''
