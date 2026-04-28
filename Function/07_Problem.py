# Q. write a program to remove a given word from a list of words.

def rem(l, word):
    n = []
    for item in l:
       if not(item == word):
            n.append(item.strip(word))

    return n    
        # l.remove(word)
        # return l


l = ["harry", "omkar", " rohan", "an" "om"]


print(rem(l, "an"))