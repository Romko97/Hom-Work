Zen = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# Знайти кількість слів у стрічці

substring = ["better", "never", "is"]
for i in range(len(substring)):
    count = Zen.count(substring[i])
    print(count)

print('\n............................\n')

# Вивести весь текст у верхньому регістрі.

# upperString = Zen.upper()
# print(upperString)

print(Zen.upper())

print('\n............................\n')

# Замінити всі літери "і" на "&"

# replaced_i_to_ampersand = Zen.replace('i', '&')
# print(replaced_i_to_ampersand)

print(Zen.replace('i', '&'))

print('\n............................\n')

# Задано чотирицифрове натуральне число.
# first way of solution
# Знайти добуток цифр цього числа.

number = int(input("Please enter nnumber :"))
changed_type = str(number)
product = 1
for i in range(len(changed_type)):
    product *= int(changed_type[i])
print("product is :", product)

print('\n............................\n')

# Записати число в реверсному порядку.
# the first way of solution

print('\n.first way of solution \n')

changed_type = str(number)
print(list(reversed(changed_type)))

# the second way of solution.
print('\n.second way of solution \n')
originNumber = number
Reverse = 0
while (number > 0):
    Reminder = number % 10
    Reverse = (Reverse * 10) + Reminder
    number //= 10
print(f"Revers of {originNumber} is {Reverse}")

print('\n............................\n')

print("the third way of solution\n")

number = input("enter number again:")
print(number[::-1])

# Посортувати цифри, що входять в дане число

print(sorted(number))

print('\n............................\n')
# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = input("first var: ")
b = input("second var: ")
# print(f"first var:{a} \nsecond var: {b}")
a, b = b, a
print(f"first var:{a} \nsecond var: {b}")
