# """   UDACIFY QUIZ -1   """

# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'


def udacify(udacity):
    udacify = "U"
    return udacify + udacity


print(udacify("dacians"))
# --------------------------> RESULT Udacians

# ######################################################################################################################


# """   MEDIAN QUIZ -3   """

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.
# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b


def biggest(a,b,c):
    return bigger(a,bigger(b,c))


def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)


print(median(9,3,6))
print(median(7,8,7))
# --------------------------> RESULT 6 7

# ######################################################################################################################


# """   BLASTOFF QUIZ -4   """

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).
def countdown(n):
    while n >= 1:
        print(n)
        n = n-1
        if n == 0:
            print("Blastoff!")


countdown(3)
# --------------------------> RESULT 3 2 1 Blastoff!

# ######################################################################################################################


# """   FIND LAST QUIZ -6   """

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
# Make sure your procedure has a return statement.

def find_last(search,target):
    return search.rfind(target)


print(find_last('aaaaa', 'aa'))
print(find_last('aaaa', 'b'))
print(find_last("222222222", ""))
print(find_last("", "3"))
print(find_last("", ""))
# --------------------------> RESULT 3 -1 9 -1 0

# ######################################################################################################################
