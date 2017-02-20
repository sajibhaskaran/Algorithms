



def word_replace(string, before, after):
    if before.istitle():
        after = after.title()
    result = string.replace(before, after)
    print(result)



word_replace("A quick brown fox Jumped over the lazy dog", "Jumped", "leaped")
word_replace("This has a spellngi error", "spellngi", "spelling")
