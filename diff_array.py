

def diff(lst1, lst2):
    result = []

    for i in range(len(lst1)):        
        if not lst1[i] in lst2:
            
            result.append(lst1[i])

    for i in range(len(lst2)):        
        if not lst2[i] in lst1:
            
            result.append(lst2[i])
                  
          

        
    print(result)

diff([1, 2, 3, 5], [1, 2, 3, 4, 5])
