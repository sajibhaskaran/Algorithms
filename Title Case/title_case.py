# Purpose : Title Case a Sentence
#         : Return the provided string with the first letter of each word capitalized.
#         : Make sure the rest of the word is in lower case.
# Author  : Saji Bhaskaran

def title_case(str):
    #str = str.lower()
    str = ' '.join(word[0].upper() + word[1:].lower() for word in str.split())
    print(str)

title_case("I'm a little tea pot")
title_case("HERE IS MY HANDLE HERE IS MY SPOUT")
