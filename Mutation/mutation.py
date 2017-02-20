# Purpose : Return true if the string in the first element of the array contains all
#         : of the letters of the string in the second element of the array.
#
# Author  : Saji Bhaskaran


def mutation(lst):
    x = [i.lower() for i in lst]
    for i in x[0]:
        a = x[1].find(i)
        if a == -1:
            return False
            break;
    return True         
                
        

   

print(mutation(["hello", "Hello"]))
print(mutation(["hello", "hey"]))
print(mutation(["Mary", "Aarmy"]))

    
