

def cipher_13(str):
    lst = [ord(c) for c in str]
    new_lst =[]
    for i in lst:        
        if 64 < i < 91:
            if (i + 13) > 90:
                i = 64 + ((i + 13)-90)
            else:
                i = i + 13
        new_lst.append(i)                
          
    new_lst = ''.join([chr(c) for c in new_lst])          
       
        
    print(new_lst)



cipher_13("SERR YBIR?")
cipher_13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.")
