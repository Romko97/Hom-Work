'''

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
'''
'''
def division():
    """divids numbers"""
    lis = []
    d = input("Enter numbers then 'D' for divition\n=:")
    while d.lower != 'd':
        lis.append(d)
        d = input("next number: ")
        if d == 'd':
            for i in range(len(lis)):
                lis[i] = float(lis[i])
            d = lis[0]
            for i in range(1, len(lis)):
                d = d/lis[i]
                print(f"/{lis[i]}=",d)
            return d
        else:
            continue
'''


def division(*args):
    new = []
    for args in input('Введіть числа для ділення: ').split():
        num = float(args)
        new.append(num)
    new_num = 0
    for _ in new:
        if new_num != [1]:
            new_num = new[0] / new[1]
            del new[:2]
            new.append(new_num)
            new = new[::-1]
    print(f'Частка чисел:{new[0]}\n')



division()