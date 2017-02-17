

def cipher_13(str):
    lst = [ord(c) for c in str]
    new_lst =[]
    for i in lst:        
        if 65 < i < 90:
            i = 65 + (i -90)
        new_lst.append(i+32)
    new_lst = [chr(c) for c in new_lst]
            

    
        
    
    print(lst)
    print(new_lst)



cipher_13("SAJI BHASKARAN")
