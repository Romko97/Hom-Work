
# 1.  Написати функцію, яка знаходить середнє арифметичне
# значення довільної кількості чисел.


def fung(*args):
    print(sum(args)/len(args))


'''
fung(2,24,69)
'''


# 2 .  Написати функцію, яка повертає абсолютне значення числа

def modul(num):
    """DocString"""
    if num >= 0:
        return num
    else:
        return -num


'''
print(modul(-5))
'''

# 3.  Написати функцію, яка знаходить максимальне число з
#  двох чисел, а також в функції використати рядки документації DocStrings.


def maximum(a, b):
    '''looking max number'''
    if a > b:
        print(a)
    elif a == b:
        print(f"{a}={b}")
    else:
        print(b)


'''
maximum(2, 1)
'''

# 4.  Написати програму, яка обчислює площу прямокутника,
# # трикутника та кола (написати три функції для обчислення площі,
#  і викликати їх в головній програмі в залежності від вибору користувача)


def triangle(a, h):
    '''calculat the area of the triangle '''
    S = 0.5 * a * h
    return S


def rectangle(a, b):
    '''calculat the area of the rectangle'''
    S = a * b
    return S


def circle(r):
    '''calculat the area of the circle'''
    p = 3.14159265358979
    S = p * r ** 2
    return S


def choice():
    '''Calculat the area of the triangle, rectangle, circle'''
    choice = int(input("Please make chois\n[1]-trianglr\n[2]-rectangle\n[3]-circle.\n:"))
    if choice == 1:
        a = int(input('enter basis:'))
        b = int(input('enter hight:'))
        return triangle(a, b)
    elif choice == 2:
        a = int(input('enter side a:'))
        b = int(input('enter side b:'))
        return rectangle(a, b)
    elif choice == 3:
        r = int(input('enter radius r:'))
        return circle(r)
    else:
        print("wrong choice")


'''
print(choice())
'''


def rectangle2():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    print("Square={}".format(a*b))


def triangle2():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    print("Area={}".format(0.5 * a * h))


def circle2():
    PI = 3.14
    r = float(input("Input radius: "))
    print("Square={}".format(PI * r**2))

'''
figure = input("1-rectangle, 2-triangle, 3-circle: ")
if figure == '1':
    rectangle2()
elif figure == '2':
    triangle2()
elif figure == '3':
    circle2()
else:
    print("Input error")
'''

# 5.  Написати функцію, яка обчислює суму цифр введеного числа.


def sum_of_digit_of_umber(number):
    '''calculates the sum of the digits of
    the number entered'''
    number = str(number)
    n = 0
    for i in number:
        n += int(number[1])
    print(n)

'''
sum_of_digit_of_umber(123)
'''
#############################################


def sumD(n):
    sum = 0
    while n != 0:
       sum += n % 10
       n = n // 10
    return sum


print(sumD(123))

# 6.  Написати програму калькулятор, яка складається з наступних функцій:
# # головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані
# дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора,
# після виходу, користувач отримує повідомлення з подякою за вибір нашого
# програмного продукту!!!


def main():
    """prompts you to choose an action"""
    figure = ''
    while figure.lower() != 'e':
        figure = input("1-addition\n2-subtration\n3-multiplication\n4-division\n:'\ne-exit")
        if figure == '1':
            print(addition())
        elif figure == '2':
            print(subtraction())
        elif figure == '3':
            print(multiplication())
        elif figure == '4':
            print(division())
        elif figure.lower() == 'e':
            print(exit_from_program())
        else:
            print("Input error")


def addition():
    """adds two numbers"""
    a = float(input("augend+ "))
    b = float(input("+addend: "))
    return f"{a} + {b} = {a + b}"


def subtraction():
    """subtracts two numbers"""
    a = float(input(": "))
    b = float(input(": "))
    return f"{a} - {b} = {a - b}"


def multiplication():
    """multiply two numbers"""
    a = float(input(": "))
    b = float(input(": "))
    return f"{a} * {b} = {a * b}"


def division():
    """divids two numbers"""
    a = float(input(": "))
    b = float(input(": "))
    return f"{a} / {b} = {a / b}"


def exit_from_program():
    return "Thenk you for choosig our program"

'''
main()
'''

# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа
# введеного користувачем.


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


'''
a = int(input("Enter the number for generat sequence of namber Fibonacci:"))
print(fibonacci(a))
'''

# 8.  Написати програму, яка обчислює
# дискримінант квадратного рівняння


def discriminator(a, b, c):
    print(f"D = {b}^2-4*{a}*{c}")
    return b ** 2 - 4 * a * c

'''
print("((a*x)^2)+(b*x)+c=0")
print("enter the coeficients:")
a1 = float(input("a = "))
b1 = float(input("b = "))
c1 = float(input("c = "))
print(f"(({a1} x)**2)+({b1}*x)+{c1} = 0")
print("D = ", discriminator(a1, b1, c1))
'''

