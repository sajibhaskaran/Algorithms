

def pair(string):
    match = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
        }
    result = []

    for c in string:
        templst = [c, match[c]]
        result.append(templst)

    print(result)


pair("GCG")
