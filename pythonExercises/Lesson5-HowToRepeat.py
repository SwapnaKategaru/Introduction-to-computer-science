# """   ABBAIZE QUIZ -14   """

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.


def abbaize(string1, string2):
    return string1 + string2 * 2 + string1


print(abbaize('a','b'))
# --------------------------> RESULT abba

# ######################################################################################################################


# """   FIND SECOND QUIZ -15   """

# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.
danton = "De l'audace, encore de l'audace, toujours de l'audace"


def find_second(search, target):
    target_1 = search.find(target)
    target_2 = search.find(target, target_1 + 1)
    return target_2


print(find_second(danton, "audace"))
# --------------------------> RESULT 25

# ######################################################################################################################


# """   IF STATEMENTS QUIZ -17   """

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(x, y):
    if x > y:
        return x
    else:
        return y


print(bigger(3, 18))
# --------------------------> RESULT 18

# ######################################################################################################################


# """   IS FRIEND QUIZ -18   """

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(pal):
    if pal[0] == "D" or pal[0] == "d":
        return True
    else:
        return False


print(is_friend('Diane'))
print(is_friend('Fred'))
# --------------------------> RESULT True & False

# ######################################################################################################################


# """   MORE FRIENDS QUIZ -19   """

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
    if name[0] == 'D' or name[0] == 'N':
        return True
    return False


print(is_friend('Diane'))
print(is_friend('Ned'))
print(is_friend('Moe'))
# --------------------------> RESULT True & True & False

# ######################################################################################################################


# """   BIGGEST QUIZ -21   """

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    return c


print(biggest(6, 3, 9))
# --------------------------> RESULT 9

# ######################################################################################################################


# """   PRINT NUMBERS QUIZ -24   """

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.
# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    i = 0
    while i < n:
        i = i + 1
        print(i)


print(print_numbers(3))
# --------------------------> RESULT 1 2 3 None

# ######################################################################################################################

# """   FACTORIAL QUIZ -25   """

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.


def factorial(n):
    i = 1
    while n >= 1:
        i = i * n
        n = n - 1
    return i


print(factorial(5))
# --------------------------> RESULT 120

# ######################################################################################################################
