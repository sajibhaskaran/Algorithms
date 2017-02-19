



def convert(num):
    roman_numerals = { 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                       'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1 }

    sorted_lst = sorted(roman_numerals.items(), key=lambda x: x[1], reverse=True)
     
    roman_num =""
    if num > 0:
        for i in sorted_lst:
            while num >= i[1]:
                roman_num += i[0]
                num -= i[1]
    else:
        print("Number need to be bigger than 0")                
             
    print(roman_num)
     



convert(649)
convert(8999)
