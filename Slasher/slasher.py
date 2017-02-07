# Purpose : Return the remaining elements of a list after chopping off
#         : n elements from the head.
#
# Author  : Saji Bhaskaran


def slasher(lst, num):
    slashed = lst[num:]
    print(slashed)


slasher([1, 2, 3], 4)
slasher([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5)



    
