# Purpose : Sum All Numbers in a Range
#         : Return the sum of those two numbers and all numbers between them.
#
# Author  : Saji Bhaskaran



def sum_all(lst):
    sum = 0;
    for i in range(min(lst), max(lst)+1):
        sum += i

    print(sum)


sum_all([1,4])        
sum_all([10, 5])
