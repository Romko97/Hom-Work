# Given an array of integers.
# Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you
# should return [10, -65].


def count_positives_sum_negatives(arr):
    a, b = 0, 0
    lis = []
    if arr == []:
        return []
    for i in arr:
        if i > 0:
            print()
            a += 1
        else:
            b += i
    lis.append(a)
    lis.append(b)
    return lis


def is_beter(arr):
    if not arr: return []
    pos, neg = 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        else:
            neg += i
    return [pos, neg]


def is_clever(arr):
    return [len([i for i in arr if i > 0])] + [sum(i for i in arr if i < 0)] if arr else []


print(count_positives_sum_negatives([76, -15, 17, 62, -53, 69, -50, -80, 74, 19, 67, 99, -76, -69, 87, -52, 75, 39, 17, -61, -29]))
print(is_beter([76, -15, 17, 62, -53, 69, -50, -80, 74, 19, 67, 99, -76, -69, 87, -52, 75, 39, 17, -61, -29]))
print(is_clever([76, -15, 17, 62, -53, 69, -50, -80, 74, 19, 67, 99, -76, -69, 87, -52, 75, 39, 17, -61, -29]))
 
 # ого о_О


 # Reverse List Order 
 # In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
    return l[::-1]


def reverse_list1(l):
    return list(reversed(l))


reverse_list2 = lambda l: l[::-1]


print(reverse_list([1,2,3,4]))
print(reverse_list1([1,2,3,4]))
print(reverse_list2([1,2,3,4]))

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5
# below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
    a = 0
    for i in range(1,number):
        if i % 3 == 0:
            a += i   
        elif i % 5 == 0:
            a += i    
    return a


def is_betterone(number):
    return sum(i for i in range(number) if i % 3 ==0 or i % 5 == 0)


def solution_clever(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3 * (a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result


print(solution(10)) # 23)
print(is_betterone(10)) # 23)
print(solution_clever(10))   # 23.4000000000002 але чому ????
