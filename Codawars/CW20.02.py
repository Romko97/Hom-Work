# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0


def summation(num):
    return sum(i for i in range(1,num+1))


print(summation(8))


# Your collegue wrote an simple loop to list his favourite animals.
# But there seems to be a minor mistake in the grammar,
# which prevents the program to work. Fix it! :)

# If you pass the list of your favourite animals to the function, you should
# get the list of the animals with orderings and newlines added.

# For example, passing in:

# animals = [ 'dog', 'cat', 'elephant' ]
# will result in:

# list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'
'''
def list_animals(animals):
    list = ''
    for i in range(animals):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list
'''
def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


animals = [ 'dog', 'cat', 'elephant' ]
print(list_animals(animals))

# Given a string, you have to return a string in which each
# character (case-sensitive) is repeated once.


def double_char(s):
    result = ''
    for i in s :
        result += i*2
    return result


print(double_char("String"))


def aaaaaaaa(s):
    return ''.join(i *2 for i in s)


print(aaaaaaaa("String"))