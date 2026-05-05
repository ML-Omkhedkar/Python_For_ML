

# words = ["omkar" , "coming" , "twinkle" , "ho"]   

# with open("file.txt" , "r") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word , "#" * len(word))

# with open("file.txt" , "w") as f:
#     f.write(content)


words = ["Donkey" , "omkar", "harry" , "bhai"]

with open("file.txt" , "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "@" * len(word))

with open("file.txt" , "w") as f:
    f.write(content)





















































