# """   TEXT REPLACEMENT QUIZ -2   """

# Write a program that takes a line of text and
# finds the first occurrence of a certain marker
# and replaces it with a replacement text.
# The resulting line of text should be stored in a variable.
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."
replaced = line.replace(marker, replacement)
print(replaced)
# --------------------------> RESULT I will now go to sleep and be away from keyboard until lunch time tomorrow.


