# Regular Ball Super Ball
# Create a class Ball.
# Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

"""
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
"""

# Color Ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of white" or
# "yellow" or "purple" or "red" when instantiated
"""
import random
class Ghost(object):
  colors = ["white", "yellow", "purple", "red"]
  def __init__(self):
    self.color = random.choice(Ghost.colors)"""


# According to the creation myths of the Abrahamic religions,
# Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array
# of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have
# to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.


class Human:
    def __init__(self):
        pass
class Man(Human):
    def __init__(self):
        pass
class Woman(Human):
    def __init__(self):
        pass

def God():
    Adam = Man()
    Eva = Woman()
    return [Adam,Eva]


# Classy Classes
# Basic Classes, this kata is mainly aimed at the new JS
# ES6 Update introducing classes
# Task
# Your task is to complete this Class, the Person class has
# been created. You must fill in the Constructor method to
# accept a name as string and an age as number, complete the
# get Info property and getInfo method/Info getter which should return


class Person:
    def __init__(self,name,age):
        self.info = f"{name}s age is {str(age)}"