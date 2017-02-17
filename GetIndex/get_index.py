# Purpose : Return the lowest index at which a value (second argument) should be inserted
#         : into an array (first argument) once it has been sorted. 
#         : The returned value should be a number.
#
# Author  : Saji Bhaskaran


def get_index(lst, num):
    lst.append(num)
    lst.sort()
    print(lst.index(num))




get_index([10, 20, 30, 40, 50], 35)
get_index([10, 20, 30, 40, 50], 30)
get_index([3, 10, 5], 2)


