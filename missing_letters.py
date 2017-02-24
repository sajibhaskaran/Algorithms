

def missing_letter(string):
    word = ''
    start = ord(string[0])
    end = ord(string[-1])
    for i in range(start, end+1):
        if string.find(chr(i)) == -1:
            return chr(i)
    return "undefined"   
        
        

    
print(missing_letter('abc'))
