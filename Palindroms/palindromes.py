#
#
#
#

import re

def palindrome(str):
    
    str1 = re.sub(r"[^\w\s]", '', str)
    str2 = re.sub(r"[\s+\_]", '', str1)
    str3 = str2.lower()
    str4 = str3[::-1]
    if str3 == str4:
        print("yes, it is a palindrome")
    else:
        print("no, it is not a palindrome")


palindrome("A man, a: plan, (a). -canal. Panama_");
palindrome("1 eye for of 1 eye.")

