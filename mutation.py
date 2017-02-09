

def mutation(lst):
    x = [i.lower() for i in lst]
    for i in x[0]:
        a = x[1].find(i)
        if a == -1:
            return False
            break;
    return True
           
    
                
        

    #print(x)

print(mutation(["hello", "Hello"]))
print(mutation(["hello", "hey"]))
print(mutation(["Mary", "Aarmy"]))

    
