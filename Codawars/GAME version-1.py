
# The game
# In this game, there are 21 sticks lying in a pile. Players take turns taking
# 1, 2, or 3 sticks. The last person to take a stick wins. For example:
# Your task
# Create a robot that will always win the game.
# Your robot will always go first.
# The function should take an integer and returns 1, 2, or 3.
# Note: The input will always be valid (a positive integer)


sticks_exist = 21



def make_move(sticks):
    ''' subtracts 1 or 2 or 3 sticks '''
    global sticks_exist
    if user_make_move <= 0 or user_make_move > 3:
        print("try agen")
    else:
        sticks_exist -= sticks

        
    return sticks
    


def robot_make_move():
    global sticks_exist
    global user_make_move
    print( "my torn ", sticks_exist % 4)
    sticks_exist -= (sticks_exist % 4)
    return sticks_exist
    

robot_make_move()
while sticks_exist > 0:
    user_make_move = int(input("how many sticks you take? 1, 2 or 3 : "))
    print(make_move(user_make_move))
    print(robot_make_move())
else:
    print("ROBOT  win")