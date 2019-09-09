# """   WORD COUNT QUIZ - 1   """

# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.


def count_words():
    words = passage.split()
    return len(words)


passage = ("The number of orderings of the 52 cards in a deck of cards "
           "is so great that if every one of the almost 7 billion people alive "
           "today dealt one ordering of the cards per second, it would take "
           "2.5 * 10**40 times the age of the universe to order the cards in every "
           "possible way.")
print(count_words())
# --------------------------> RESULT 56

# ######################################################################################################################


# """   LATENCY QUIZ - 2   """

# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.  # km per second


def speed_fraction(time, dist):
    x = (float(2) * dist) / time
    y = speed_of_light / 1000
    return x / y


print(speed_fraction(50, 5000))
print(speed_fraction(50, 10000))
# --------------------------> RESULT  0.666666666667, 1.33333333333

# ######################################################################################################################


# """   CONVERTING SECONDS QUIZ - 3   """

# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".


def convert_seconds(num):
    hours = int(num) // (60 * 60)
    min = num % (60 * 60)
    minutes = int(min) // 60
    sec = min % 60
    seconds = sec / 1
    if hours and minutes and seconds == 1:
        return "{} hour, {} minute, {} second".format(hours, minutes, seconds)
    elif hours == 1 and minutes == 0:
        return "{} hour, {} minutes, {} seconds".format(hours, minutes, seconds)
    elif minutes == 1:
        return "{} hours, {} minute, {} seconds".format(hours, minutes, seconds)
    elif minutes == 0 and seconds == 1:
        return "{} hours, {} minutes, {} second".format(hours, minutes, seconds)
    else:
        return "{} hours, {} minutes, {} seconds".format(hours, minutes, seconds)


print(convert_seconds(3661))

print(convert_seconds(7325))

print(convert_seconds(7261.7))
# --------------------------> RESULT  1 hour, 1 minute, 1 second
#                                     2 hours, 2 minutes, 5 seconds
#                                     2 hours, 1 minute, 1.7 seconds

# ######################################################################################################################
