# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число
# з діапазону чисел від 1 до 100 і пропонує користувачу вгадати
# це число. Програма зчитує числа, які вводить користувач і видає
# користувачу підказки про те чи загадане число більше чи менше за
# введене користувачем. Гра має тривати до моменту поки користувач не
# введе число, яке загадане програмою, тоді друкує повідомлення привітання.

# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())
import random
from math import pow
from math import pi



random_number = random.randint(0, 50)
user = -1
while user != random_number:
    user = int(input("try gase :"))
    if user > random_number:
        print('thet number is lower ')
    elif user < random_number:
        print(' thet number is biger')
    else:
        print('congrads you gased')


'''
number=random.randint(1,100)
while True:
    guess=int(input("Please guess the number between 1 and 100:\n"))
    if i==number:
        print("You guessed!!!")
        break
    elif i<number:
        print("Choose a larger number")
    elif i>number:
        print("Choose a smaller number")        
'''
#2.  Напишіть скрипт, який обчислює площу прямокутника a*b,
# площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math,
# а з нього функцію pow() та значення змінної пі).



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
    S = pi * pow(r, 2)
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



print(choice())
