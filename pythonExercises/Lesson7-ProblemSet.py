# """   WEEKEND QUIZ -1   """

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.


def weekend(day):
    if day == "Saturday" or day == "Sunday":
        return True
    return False


print(weekend("Monday"))
print(weekend('Saturday'))
print(weekend('July'))
# --------------------------> RESULT False True False

# ######################################################################################################################


# """   STAMPS QUIZ -2   """

# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.

def stamps(n):
    five = n // 5
    remaining_1 = n % 5
    two = remaining_1 // 2
    remaining_2 = remaining_1 % 2
    one = remaining_2 // 1
    return five, two, one


print(stamps(8))
# >>> (1, 1, 1)
print(stamps(5))
# >>> (1, 0, 0)
print(stamps(29))
# >>> (5, 2, 0)
print(stamps(0))
# >>> (0, 0, 0)
# --------------------------> RESULT (1, 1, 1) (1, 0, 0) (5, 2, 0) (0, 0, 0)

# ######################################################################################################################


"""   RANGE OF A SET QUIZ - 3   """

# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.


def set_range(a, b, c):
    if a > b and a > c:
        bigger = a
        if b < c:
            smaller = b
        else:
            smaller = c
    elif b > c:
        bigger = b
        if c < a:
            smaller = c
        else:
            smaller = a
    else:
        bigger = c
        if a > b:
            smaller = b
        else:
            smaller = a
    return bigger - smaller

# ######### OR #########


def set_range(a, b, c):
    return max(a, b, c) - min(a, b, c)


print(set_range(10, 4, 7))
print(set_range(1.1, 7.4, 18.7))
# --------------------------> RESULT 6 and 17.6

# ######################################################################################################################


