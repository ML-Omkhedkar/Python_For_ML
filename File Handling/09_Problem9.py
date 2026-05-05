
with open("this.txt") as f:
    content = f.read()

with open("copy_this.txt") as f:
    content2 = f.read()


if content == content2:
    print("yes this is a same file ")

else:
    print("no this is no a same file")          