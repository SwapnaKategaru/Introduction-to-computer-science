# """   PRODUCT LIST Quiz - 3   """

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.


def product_list(list_of_numbers):
    initial_num = 1
    index = 0
    while index < len(list_of_numbers):
        initial_num = initial_num * list_of_numbers[index]
        index = index + 1
    return initial_num


print(product_list([9]))
print(product_list([1, 2, 3, 4]))
print(product_list([]))
# --------------------------> RESULT 9, 24, 1

# ######################################################################################################################


# """   GREATEST QUIZ - 4   """

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


def greatest(list_of_numbers):
    greater_number = 0
    for item in list_of_numbers:
        if item > greater_number:
            greater_number = item
    return greater_number


print(greatest([4, 23, 1]))
print(greatest([]))
# --------------------------> RESULT 23, 0

# ######################################################################################################################


# """   LISTS OF LISTS Quiz - 5   """

# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string,
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity', 90000, 0]]

usa_univs = [['California Institute of Technology', 2175, 37704],
             ['Harvard', 19627, 39849],
             ['Massachusetts Institute of Technology', 10566, 40732],
             ['Princeton', 7802, 37000],
             ['Rice', 5879, 35551],
             ['Stanford', 19535, 40569],
             ['Yale', 11701, 40500]]


def total_enrollment(usa_univs):
    total_students = 0
    fee = 0
    for item in usa_univs:
        total_students = total_students + item[1]
        fee = fee + item[1] * item[2]
    return total_students, fee


print(total_enrollment(udacious_univs))
print(total_enrollment(usa_univs))
# --------------------------> RESULT (90000,0), (77285,3058581079)

# ######################################################################################################################


# """   MAX PAGES Quiz - 6   """

# The web crawler we built at the end of Unit 3 has some serious
# flaws if we were going to use it in a real crawler. One
# problem is if we start with a good seed page, it might
# run for an extremely long time (even forever, since the
# number of URLS on the web is not actually finite). This
# question and the following one explore two different ways
# to limit the pages that it can crawl.

# Modify the crawl_web procedure to take a second parameter,
# max_pages, that limits the number of pages to crawl.
# Your procedure should terminate the crawl after
# max_pages different pages have been crawled, or when
# there are no more pages to crawl.

# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
                    '<p> It is a good idea to '
                    '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                    'crawl</a> before you try to  '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                    'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
                    'am quite good at '
                    '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
                    '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
                    '</body> </html>')
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


print(crawl_web("http://www.udacity.com/cs101x/index.html", 1))
print(crawl_web("http://www.udacity.com/cs101x/index.html", 3))
print(crawl_web("http://www.udacity.com/cs101x/index.html", 500))
# --------------------------> RESULT ['http://www.udacity.com/cs101x/index.html']

#                                    ['http://www.udacity.com/cs101x/index.html',
#                                     'http://www.udacity.com/cs101x/flying.html',
#                                     'http://www.udacity.com/cs101x/walking.html']

#                                    ['http://www.udacity.com/cs101x/index.html',
#                                     'http://www.udacity.com/cs101x/flying.html',
#                                     'http://www.udacity.com/cs101x/walking.html',
#                                     'http://www.udacity.com/cs101x/crawling.html',
#                                     'http://www.udacity.com/cs101x/kicking.html']

# ######################################################################################################################


# """   MAX DEPTH - 7   """

# Modify the crawl_web procedure to take a second parameter,
# max_depth, that limits the depth of the search.  We can
# define the depth of a page as the number of links that must
# be followed to reach that page starting from the seed page,
# that is, the length of the shortest path from the seed to
# the page.  No pages whose depth exceeds max_depth should be
# included in the crawl.
#
# For example, if max_depth is 0, the only page that should
# be crawled is the seed page. If max_depth is 1, the pages
# that should be crawled are the seed page and every page that
# it links to directly. If max_depth is 2, the crawl should
# also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#
# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
                    '<p> It is a good idea to '
                    '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                    'crawl</a> before you try to  '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                    'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
                    'am quite good at '
                    '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
                    '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
                    '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
                    '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return ('<a href="http://top.contributors/elssar.html">'
                    '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
                    '<a href="http://top.contributors/johang.html">'
                    '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
                    '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
                    '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return '<a href="B1"> <a href="C1">'
        elif url == "B1":
            return '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1">'
        elif url == "E1":
            return '<a href="F1">'
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled


print(crawl_web("http://www.udacity.com/cs101x/index.html", 0))
print(crawl_web("http://www.udacity.com/cs101x/index.html", 1))
print(crawl_web("A1", 3))
# --------------------------> RESULT ['http://www.udacity.com/cs101x/index.html']

#                                    ['http://www.udacity.com/cs101x/index.html',
#                                     'http://www.udacity.com/cs101x/flying.html',
#                                     'http://www.udacity.com/cs101x/walking.html',
#                                     'http://www.udacity.com/cs101x/crawling.html']

#                                    ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']

# ######################################################################################################################
