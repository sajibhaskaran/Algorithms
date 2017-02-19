# Purpose : Compare two arrays and return a new array with any items only found
#         : in one of the two given arrays, but not both.
#         : In other words, return the symmetric difference of the two arrays.
#
# Author  : Saji Bhaskaran

def diff_list(lst1, lst2):
    result = []

    for i in range(len(lst1)):        
        if not lst1[i] in lst2:
            
            result.append(lst1[i])

    for i in range(len(lst2)):        
        if not lst2[i] in lst1:
            
            result.append(lst2[i])                 
    print(result)


diff_list([1, 2, 3, 5], [1, 2, 3, 4, 5])
diff_list(["andesite", "grass", "dirt", "pink wool", "dead shrub"],
          ["diorite", "andesite", "grass", "dirt", "dead shrub"])
