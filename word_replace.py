# Purpose : Perform a search and replace on the sentence using the arguments
#         : provided and return the new sentence.
#
# Author  : Saji Bhaskaran


def word_replace(string, before, after):
    if before.istitle():
        after = after.title()
    else:
        after = after[0].lower() + after[1:]
    result = string.replace(before, after)
    print(result)



word_replace("A quick brown fox Jumped over the lazy dog", "Jumped", "leaped")
word_replace("This has a spellngi error", "spellngi", "spelling")
