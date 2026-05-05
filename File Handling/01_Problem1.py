
f = open("poems.txt", "r")
file = f.read()
f.close()

if "twinkle" in file:
    print("yes twinkle is present")
else:
    print("no twinkle is not present")    

# print(file)

# Second method --- with
with open("poems.txt") as f:
    file = f.read()
    print(file)