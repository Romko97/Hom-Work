# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити
# серед них максимальне та мінімальне число.
'''
li = []
number_of_numbers = (int(input("Enter number of qwenteti list:")))
for i in range(number_of_numbers):
    a = int(input(f"enter number {i} of your list: "))
    li.append(a)
print(li, f"\nMin number is: {min(li)} \nMax number is: {max(li)}")
'''



# 2.  В інтервалі від 1 до 10 визначити числа
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3,
# •  числа, які не діляться на 2 та 3.
'''
for i in range(1, 11):
    if i % 2 == 0:
        print(i,"ділиться на 2")
    elif i % 3 == 0:
        print(i,"an odd ділиться на 3")
    else:
        print(i, 'not divisible by 2 and 3')
'''
# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)

# while
'''
number = int(input("Enter pleas number:"))
a = int(number)
while a != 1:
    number = number * (a-1)
    a = a-1
print(number)
'''

# for i in range
'''
chyslo = input('enter factorial :')
t = 1
for i in range(1, int(chyslo)+1):
    t *= i
print(t)
'''

# Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.(використайте цикл while)

'''
login = input("Your Login :")
print("You successfully registered: ", login)
while input("please log in: ") != login:
    print("Wrong login, try agen!")
print("you entered")
'''

# 5.  Перший випадок. Написати програму, яка буде зчитувати числа поки
# не зустріне від’ємне число. При появі від’ємного числа програма
# зупиняється (якщо зустрічається 0 програма теж зупиняється).
'''
List = [1, 5, 6, 9, 8, 5, 4, 0, 5, 0, 8, 5, 7, 1]
print("for")
for i in List:
    if i <= 0:
        break
    else:
        print(i)

print("Wile")
a = 0
while List[a] > 0:
    print(List[a])
    a += 1
'''

# 6.  Другий випадок.
# На початку на вхід подається кількість елементів послідовності, а потім самі
# елементи. При появі від’ємного числа програма зупиняється (якщо зустрічається
#  0 програма теж зупиняється).
'''
number = int(input('pleas enter a number how many number would you like: '))
for i in range(number):
    a = int(input("Pleas enter any number you like: "))
    if a <= 0:
        break
'''

# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити
#  у вигляді добутку чисел
# (наприклад 10 equals 2 * 5
# 11 is a prime number
# 12 equals 2 * 6
# 13 is a prime number
# 14 equals 2 * 7………………….)

'''
for a in range(10, 31):
    for b in range(2, a):
        if a % b == 0:
            c = a / b
            print(f"{a} = {b} * {c}")
            break
        else:
            if b == (a-1):
                print(a, "PRIME")
'''
'''
for num in range(10, 30):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('{0} equals {1} * {2}'.format(num, i, j))
            break
    else:
        print(num, 'is a prime number')
'''
