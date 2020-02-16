# Simple: Find The Distance Between Two Points
# Given two ordered pairs calculate the distance
#  between them. Round to two decimal places.
#  This should be easy to do in 0(1) timing.


def distance(x1, y1, x2, y2):
    """This fanction are finding the distance betvin two points"""
    print(round(((((x1-x2)**2)+((y1-y2)**2))**0.5), 2))


"""distance(1, 1, 0, 0)"""



# The game
# In this game, there are 21 sticks lying in a pile. Players take turns taking
# 1, 2, or 3 sticks. The last person to take a stick wins. For example:
# Your task
# Create a robot that will always win the game.
# Your robot will always go first.
# The function should take an integer and returns 1, 2, or 3.
# Note: The input will always be valid (a positive integer)


def make_move(stiks): print(max(stiks % 4, 1))


'''make_move(6)'''


# Write a function taking in a string like WOW this is REALLY amazing and
# returning Wow this is really amazing. String should be capitalized and
# properly spaced. Using re and string is not allowed.


def filter_words(st):
    return " ".join((st.capitalize()).split())


filter_words("HELLO    world!")
