# Purpose : Return Largest Numbers in Arrays
#         : Return an array consisting of the largest number from each provided sub-array.
#
# Author  : Saji Bhaskaran


def largest_off_four(lst):
    
    lists = []    
    for l in lst:
        lists.append(max(l))
        
    print(lists)



largest_off_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])
largest_off_four([[14, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]])
