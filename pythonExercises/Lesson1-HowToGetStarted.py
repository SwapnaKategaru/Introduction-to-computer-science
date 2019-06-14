# """"   FIRST PROGRAMMING QUIZ -7   """

# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result

print(7 * 7 * 24 * 60)
# -------------------> RESULT 70560

# ######################################################################################################################


# """"   SPEED OF LIGHT QUIZ -14   """

# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
speed_of_light = 299792458  # meters per second
centimeters = 100  # one meter is 100 centimeters
nanosecond = 1 / 1000000000.0  # one billionth of a second

print(speed_of_light * centimeters * nanosecond)
# -------------------> RESULT 29.9792458

# ######################################################################################################################


# """"   VARIABLES QUIZ -18   """

# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.
# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
print(speed_of_light / cycles_per_second)
# -------------------> RESULT 0.1110342437037037

# ######################################################################################################################


# """"   SPIRIT AGE QUIZ -22   """

# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.
age = 19
print(age * 365)
# -------------------> RESULT 6935

# ######################################################################################################################


# """"    Hello!!! QUIZ -26   """

# Define a variable, name, and assign to it a string that is your name.
name = "Ruby"
print("Hello " + name + "!")
# -------------------> RESULT Hello Ruby!

# ######################################################################################################################


# """"    Capital Udacity QUIZ -31   """

# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.
string = 'audacity'
string = string[1:]
print(string.title())
# -------------------> RESULT Udacity

# ######################################################################################################################


# """"    FINAL QUIZ -40   """

# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# url = '<a href="http://udacity.com">Hello world</a>'
# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.
# page = contents of a web page
page = ('<div id="top_bin"><div id="top_content" class="width960">''<div class="udacity float-left">'
        '<a href="http://udacity.com">')
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1: end_quote]
print(url)
# -------------------> RESULT http://udacity.com

# ######################################################################################################################

