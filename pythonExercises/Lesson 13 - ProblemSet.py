# """"   EXPLORING LIST PROPERTIES QUIZ - 1   """

# Investigating adding and appending to lists

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

list1 = list1 + [5, 6]
list2.append([5, 6])


print("showing list1 and list2:")
print(list1)
print(list2)
# -------------------> RESULT [1, 2, 3, 4, 5, 6]  and  [1, 2, 3, 4, [5, 6]]

# ######################################################################################################################


# """"   MEAN OF A LIST QUIZ - 3   """

# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

from decimal import *
getcontext().prec = 5


def list_mean(n):
    if len(n) == 1:
        i = n[0] / 1.0
    else:
        s = 0
        for item in n:
            s = s + item
        s = Decimal(s) / Decimal(len(n))
        if type(s) == float:
            return s
        else:
            s = float(s)
            return s
    return i


print(list_mean([1, 2, 3, 4]))
print(list_mean([1, 3, 4, 5, 2]))
print(list_mean([2]))
# -------------------> RESULT 2.5, 3.0, 2.0

# ######################################################################################################################
