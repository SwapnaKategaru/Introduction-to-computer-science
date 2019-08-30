# """    ADD TO INDEX Quiz - 3   """

# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []


def add_to_index(index, keyword, url):
    for item in index:
        if item[0] == keyword:
            item[1].append(url)
            return
    index.append([keyword, [url]])


add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
print(index)
# --------------------------> RESULT [['udacity', ['http://udacity.com', 'http://npr.org']],
#                                     ['computing', ['http://acm.org']]]

# ######################################################################################################################


# """   LOOKUP Quiz - 4   """

# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index, keyword):
    for item in index:
        if item[0] == keyword:
            return item[1]
    return []


print(lookup(index, 'udacity'))
# --------------------------> RESULT ['http://udacity.com', 'http://npr.org']

# ######################################################################################################################


# """   ADD PAGE TO INDEX Quiz - 6   """

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])


def lookup(index, keyword):
    for item in index:
        if item[0] == keyword:
            # print item[1]
            return item[1]
    return []


def add_page_to_index(index, url, content):
    content = content.split()
    for item in content:
        add_to_index(index, item, url)


add_page_to_index(index, 'fake.text', "This is a test")
add_page_to_index(index, 'real.text', "This is not a test")

print(index)
#  --------------------------> RESULT  [['This', ['fake.text', 'real.text']], ['is', ['fake.text', 'real.text']],
#                                       ['a', ['fake.text', 'real.text']], ['test', ['fake.text', 'real.text']],
#                                       ['not', ['real.text']]]

# ######################################################################################################################
