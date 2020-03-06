# Is the string uppercase?
# Task
# # Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
# is_uppercase("c") == False
# is_uppercase("C") == True
# is_uppercase("hello I AM DONALD") == False
# is_uppercase("HELLO I AM DONALD") == True
# is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
# is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
# In this Kata, a string is said to be in ALL CAPS
# whenever it does not contain any lowercase letter
# so any string containing no letters at all is trivially
# considered to be in ALL CAPS.
'''
def is_uppercase(inp):
    if inp.isupper(): return True 
    return False

is_uppercase("I sgksjfngAM DONALD")
'''
# "Sort My Textbooks"
# Description:
# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

# The sorting should NOT be case sensitive
"""
def sorter(textbooks):
    return sorted(textbooks, key=lambda e: e.lower())
"""

# You're re-designing a blog and the blog's posts have the
# following format for showing the date and time a post was made:

# Weekday Month Day, time e.g., Friday May 2, 7pm

# You're running out of screen real estate, and on some pages
# you want to display a shorter format, Weekday Month Day that omits the time.

# Write a function, shortenToDate, that takes the Website
# date/time in its original string format, and returns the shortened format.

# Assume shortenToDate's input will always be a string, e.g.
# "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

"""
def shorten_to_date(long_date):
    return long_date.split(',')[0]
"""