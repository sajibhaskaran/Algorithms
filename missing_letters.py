# Purpose : Find the missing letter in the passed letter range and return it.
#        : If all letters are present in the range, return undefined.
#
# Author : Saji Bhaskaran

def missing_letter(string):
    start = ord(string[0])
    end = ord(string[-1])
    
    for i in range(start, end+1):
        if string.find(chr(i)) == -1:
            return chr(i)
    return "undefined"
    
        
        

    
print(missing_letter('abd'))
print(missing_letter('abcdefghjklmno'))
