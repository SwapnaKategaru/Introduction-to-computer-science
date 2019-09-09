# """   BETTER HASH FUNCTIONS QUIZ - 19   """

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.


def hash_string(keyword, buckets):
    h = 0
    for item in keyword:
        h = (h + ord(item)) % buckets
    return h


print(hash_string('a', 12))
print(hash_string('b', 12))
print(hash_string('a', 13))
print(hash_string('au', 12))
print(hash_string('udacity', 12))
# --------------------------> RESULT 1, 2, 6, 10, 11

# ######################################################################################################################


# """   EMPTY HASH TABLE QUIZ - 23   """

# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hash_table = []
    i = 0
    while i < nbuckets:
        hash_table.append([])
        i = i + 1
    return hash_table


print(make_hashtable(5))
# --------------------------> RESULT [[], [], [], [], []]

# ######################################################################################################################


# """   FINDING BUCKETS QUIZ - 25   """

# Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
         ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print(hashtable_get_bucket(table, "Zoe"))
print(hashtable_get_bucket(table, "Brick"))
print(hashtable_get_bucket(table, "Lilith"))
# --------------------------> RESULT  [['Bill', 17], ['Zoe', 14]]
#                                     []
#                                     [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

# ######################################################################################################################


# """   ADDING KEYWORDS QUIZ - 26   """

# Define a procedure,
#
# hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in
# the correct bucket), with the correct
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable, key).append([key, value])
    return htable


def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table


table = make_hashtable(5)
hashtable_add(table, 'Bill', 17)
hashtable_add(table, 'Coach', 4)
hashtable_add(table, 'Ellis', 11)
hashtable_add(table, 'Francis', 13)
hashtable_add(table, 'Louis', 29)
hashtable_add(table, 'Nick', 2)
hashtable_add(table, 'Rochelle', 4)
hashtable_add(table, 'Zoe', 14)
print(table)
# --------------------------> RESULT  [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
#                                      [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

# ######################################################################################################################


# """   LOOKUP QUIZ - 27   """

# Define a procedure,

# hashtable_lookup(htable, key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for item in bucket:
        if item[0] == key:
            return item[1]
    return None


def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])


def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
         [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print(hashtable_lookup(table, 'Francis'))
print(hashtable_lookup(table, 'Louis'))
print(hashtable_lookup(table, 'Zoe'))
# --------------------------> RESULT  13, 29, 14

# ######################################################################################################################


# """   POPULATION QUIZ - 31   """

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

# ######################################################################################################################


# """   CHANGING LOOKUP QUIZ - 34   """

# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

# ######################################################################################################################
