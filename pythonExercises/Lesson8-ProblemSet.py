# """    Superhero Nuisance Quiz - 1   """

# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).


def fix_machine(debris, product):
    if set(debris) >= set(product):
        return product
    else:
        return "Give me something that's not useless next time."


print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == 'Give me something that\'s not useless next time.')
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
# --------------------------> RESULT Test case 1:  True
#                                    Test case 2:  True

# ######################################################################################################################


# """   Jungle Animal Quiz - 4   """

# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.


def jungle_animal(animal, my_speed):
    if animal == "cheetah":
        if my_speed > 115:
            print("Run!")
        else:
            print("Stay calm and wait!")
    elif animal == "zebra":
        print("Try to ride a zebra!")
    else:
        print("Introduce yourself!")


jungle_animal('cheetah', 30)
# --------------------------> RESULT Stay calm and wait!

# ######################################################################################################################



