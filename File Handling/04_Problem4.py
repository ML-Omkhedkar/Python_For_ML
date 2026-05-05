
word = "Donkey"
with open("file.txt" , "r") as f:
    content = f.read()

contentnew = content.replace(word , "######")    

with open("file.txt", "w") as f:
    f.write(contentnew)
       






word2 ="boy"
with open("file.txt" , "r") as f:
   content = f.read()

newContent = content.replace(word2 , "@@@@@")

with open("file.txt" , "w") as f:
    f.write(newContent)
