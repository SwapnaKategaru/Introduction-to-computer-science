# """   PYTHON PROGRAMMING 1 QUIZ -2   """

# Write Python code that prints out the number of hours in 7 weeks.
hours_in_day = 24
week_days = 7
no_of_weeks = 7
print(hours_in_day * week_days * no_of_weeks)
# --------------------------> RESULT 1176

# ######################################################################################################################


# """   SPEED OF LIGHT QUIZ -4   """

# Write Python code that stores the distance
# in meters that light travels in one
# nanosecond in the variable, nanodistance.
# These variables are defined for you:
speed_of_light = 299800000.  # meters per second
nano_per_sec = 1000000000.  # 1 billion
nanodistance = speed_of_light / nano_per_sec
print(nanodistance)
# --------------------------> RESULT 0.2998

# ######################################################################################################################


# """   BODACIOUS UDACITY  QUIZ -6   """

# Given the variables s and t defined as:
# write Python code that prints out udacious
# without using any quote characters in
# your code.
s = 'udacity'
t = 'bodacious'
print(s[0] + t[2:])
# --------------------------> RESULT udacious

# ######################################################################################################################


# """   FIND1 QUIZ -7   """

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.
text = "find word"
print(text.find("word"))
# --------------------------> RESULT 5

# ######################################################################################################################


# """   FIND2 QUIZ -8   """

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
# text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"
text = 'all zip files are compressed'
# x = text1.find("zip", 5)
# y = text2.find("zip", 5)
# print(x, y)

first_zip = text.find("zip")
print(text.find("zip", (first_zip) + 1))
# --------------------------> RESULT -1

# ######################################################################################################################


# """   ROUNDING NUMBERS QUIZ -9   """

# Given a variable, x, that stores the
# value of any decimal number, write Python
# code that prints out the nearest whole
# number to x.
# If x is exactly half way between two
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.
x = 383.89327
x = round(x)
print(int(x))
# --------------------------> RESULT 384

# ######################################################################################################################
