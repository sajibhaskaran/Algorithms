# Purpose : The DNA strand is missing the pairing element.
#         : Take each character, get its pair, and return the results as a 2d array.
#         : Base pairs are a pair of AT and CG. Match the missing element to the provided character.
# Author  : Saji Bhaskaran


def pair_element(string):
    match = {"A" : "T","T" : "A","C" : "G","G" : "C"}
    result = []

    for c in string:
        templst = [c, match[c]]
        result.append(templst)

    print(result)


pair_element("GCG")
pair_element("TTGAG")
