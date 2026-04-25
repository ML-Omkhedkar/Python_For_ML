from random import randint

# This id my Frist Project In Python
# I will try to make Random Number Gueesing Game

Comp = randint(1,100)
User = int(input("Guees The Right No between 1 to 100: "))


if Comp == User:
    print(f"You Guess The {User} Right Number")
elif Comp > User:
    print("Number Is Bigger")
else:
    print(" Guese Smaller Number")

# Maine Abhi Loop Nhi seekhe So isse mai loop mai nhi chal sakta Loops seekhne ke baad Iska better Version Banalunga. 
