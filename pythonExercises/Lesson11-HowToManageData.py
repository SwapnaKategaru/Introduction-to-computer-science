# """   DAYS IN A MONTH QUIZ -3   """

# Given the variable,

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.


def how_many_days(month_number):
    i = 1
    while i < 13:
        if month_number == i:
            return days_in_month[i-1]
        else:
            i = i + 1


print(how_many_days(1))
print(how_many_days(9))
# --------------------------> RESULT 31, 30

# ######################################################################################################################


# """   COUNTRIES QUIZ - 5   """

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]

# Write code to print out the capital of India
# by accessing the list
print(countries[1][1])
# --------------------------> RESULT Delhi

# ######################################################################################################################


# """   RELATIVE SIZE QUIZ - 6   """

# Given the variable countries defined as:

#             Name      Capital  Populations (millions)
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).

china = countries[0][2]
romania = countries[2][2]
no_of_times = float(china) / float(romania)
print(no_of_times)
# --------------------------> RESULT  64.2857142857

# ######################################################################################################################


# """   DIFFERENT STOOGES QUIZ - 9   """

# We defined:

stooges = ['Moe', 'Larry', 'Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:
# ['Moe','Larry','Shemp']

# but does not create a new List object.

stooges[2] = 'Shemp'
print(stooges)
# --------------------------> RESULT ['Moe', 'Larry', 'Shemp']

# ######################################################################################################################


# """   REPLACE SPY QUIZ - 13   """

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0, 0, 7]


def replace_spy(spy):
    spy[2] = spy[2] + 1


replace_spy(spy)
print(spy)
# --------------------------> RESULT [0,0,8]

# ######################################################################################################################


# """   SUM LIST QUIZ - 24   """

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.


def sum_list(list):
    list = list[0] + list[1] + list[2]
    return list

# ####################  OR  ####################


def sum_list(list):
    i = 0
    for variable in list:
        i = i + variable
    return i


print(sum_list([1, 7, 4]))
print(sum_list([44, 14, 76]))
# --------------------------> RESULT 12, 134

# ######################################################################################################################


# """   MEASURE UDACITY QUIZ - 25   """

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(names):
    count = 0
    for name in names:
        if name[0] == "U":
            count = count + 1
    return count


print(measure_udacity(['Dave', 'Sebastian', 'Katy']))
print(measure_udacity(['Umika', 'Umberto']))
# --------------------------> RESULT  0, 2

# ######################################################################################################################


# """   FIND ELEMENT QUIZ - 26   """

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list, item_in_list):
    index = 0
    for item in list:
        if item_in_list in list:
            if item == item_in_list:
                return index
            else:
                index = index + 1
        else:
            return -1


print(find_element([1, 2, 3], 3))
print(find_element(['alpha', 'beta'], 'gamma'))
# --------------------------> RESULT  2, -1

# ######################################################################################################################


# """   INDEX QUIZ - 27   """

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(search, target):
    value = 0
    for item in search:
        if target in search:
            if item == target:
                return search.index(target)
            else:
                value += 1
        else:
            return -1


# ####################  OR  ####################


def find_element(search, target):
    if target in search:
        return search.index(target)
    else:
        return -1


print(find_element([1, 2, 3], 3))
print(find_element(['alpha', 'beta'], 'gamma'))
# --------------------------> RESULT  2, -1

# ######################################################################################################################


# """   UNION QUIZ - 29   """

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.

set_1 = [1, 2, 3]
set_2 = [2, 4, 6]


def union(set_1, set_2):
    for item in set_2:
        i = 0
        while i <= len(set_2):
            if item not in set_1:
                set_1.append(item)
            i = i + 1


union(set_1, set_2)
print(set_1)
print(set_2)
# --------------------------> RESULT  [1,2,3,4,6], [2,4,6]

# ######################################################################################################################
