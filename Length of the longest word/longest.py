# Purpose : Find the Longest Word in a String
#
#
# Author  : Saji Bhaskaran


def find_longest_word(str):
    strList = [len(x) for x in str.split()]
    print("Length of the longest word: {}".format(max(strList)))




find_longest_word("What if we try a super-long word such as otorhinolaryngology")
find_longest_word("May the force be with you")
