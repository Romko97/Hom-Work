# class CustomError(Exception): 
#     def __init__(self, data): 
#         selfdata = data
#     def __str__(self):
#         return repr(selfdata)

# Total_Score = int(input("Enter expert score: "))
# try:
#     Num_of_Group = int(input("Enter number of your group: "))
#     if Num_of_Group < 1:
#         raise CustomError("Number of your group can't be less than 1")
        
# except CustomError as e:
#     print("We obtain error:", edata) 

# 1  Напишіть програму, яка пропонує користувачу ввести ціле число
# і визначає чи це число парне чи непарне, чи введені дані коректні

'''
try:
    number = int(input("Enter a integer number : "))
    if  number % 2 == 0:
        print("enent number")
    else:
        print ('odd number')
except ValueError:
    print(" number is not number")
'''
# 2  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого
# виводить повідомлення про те чи вік є парним чи непарним числом Необхідно передбачити
# можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію 
# оловний код має викликати функцію, яка обробляє введену інформацію
'''
try:
    UserAge = int(input("Hello, User!!! How old are you? : "))
    if UserAge < 0:
        raise ValueError
    
    if  UserAge % 2 == 0:
        print("enent number")
        
    else:
        print ('odd number')
except ValueError:
    print("hahha very fany")
except:
    print("anather error")

'''

#3  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем
# послідовно через кому, передбачити випадок ділення на нуль, випадки синтаксичних
# помилок та випадки інших виняткових ситуацій Використати блоки else та finaly

'''
try:
    num1, num2 = eval(input("Enter two numbers: "))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Division by 0 is error")
except:
    print("Wrong input")
else:
    print("no exceptions ")
finally:
    print("Good")
'''

#4  Написати  програму, яка аналізує введене число та в залежності від числа видає
# день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і тд) 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних
try:
    week = {
    '1':'Mon',
    '2':'Tue',
    '3':'Wed',
    '4':'Thu',
    '5':'Fri',
    '6':'Sut',
    '7':'Sun'
    }
    numberday= (input("Enter from 1 to 7 number of week:"))
    print(week[numberday])
except KeyError:
    print("wrong input") 


d = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
while True:
    try:
        i = int(input('Enter the day of the week: '))
    except ValueError:
        print('You did not enter a number!')
    else:
        print(d.get(i, 'There is no such day of the week!'))

###################################

day_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
try:
    num = int(input("Enter number from 1 to 7: "))
    if num <= 0 or num > 7:
        raise IndexError("Youre number is out of range")
    print(day_list[num-1])
except ValueError:
    print("Wrong Input!")

