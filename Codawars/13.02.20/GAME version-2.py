sticks_exist = 21


def make_move(sticks):
    ''' subtracts 1 or 2 or 3 sticks '''
    global sticks_exist
    while sticks_exist > 0:
        sticks = int(input("how many sticks you take? 1, 2 or 3 : "))
        print("your move ", sticks,)
        sticks_exist -= sticks
        print("Left - ", sticks_exist)
        print("my torn ", sticks_exist % 4)
        sticks_exist -= (sticks_exist % 4)
    return sticks
    


make_move(int(input(":")))