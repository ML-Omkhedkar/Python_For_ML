# Q1. Separate each digit of a number and print it on the new line

# n = int(input("Enter Your Number  "))

# while n > 0:
#     print(n % 10)
#     n = n//10

# Q1 end

# Q2. Accept a number and print its reverse

# n = int(input("Enter Your Number  "))
# reverse = 0
# while n > 0:
#     reverse = (reverse *10 + n%10) 
#     n = n//10
# print(reverse)

# Q2 end

# Q3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal

# n = int(input("Checking No Is Pallindromic or not:  "))
# copy = n # making a copy of n because n is changing during the loop (so hmm n ko rev se compare nhi krr sakte loop n ko tod rha hai compare nhi ho sakta)
# rev = 0

# while n > 0:
#     rev = (rev*10 + n%10)
#     n //= 10

# print(rev)

# if copy == rev:
#     print("Your Number Is Pallindromic")
# else:
#     print("Your Number Is Not Pallindromic")    

# Q3 End

# Q4. Create a random number guessing game with python.
# iska logic to maine if else mai hi likha hai abb bss isse loop mai chalana hai (i wil try krr pata hu ki nahi)
import random 

# computer = random.randint(1,100)
# print(computer) # ye maine sirp sahi no dekhne ke liye print kiya tha program checking ke liye shi hai ya nhi....
# guess = 0
# gusses = 0
# while guess != computer: 
#     print("Guess the Number between 1 to 100")
#     guess = int(input("Enter Your Guess : "))
#     gusses += 1

#     if guess > computer:
#         print("You Guess Higher No")
#     elif guess < computer:
#         print("You Guess Lower No")
#     else:
#         print(f"you Guees Right No In {gusses} Guesses")


# i think i Did it - (yaha pe hamne kya kiya hai guees = 0  hai jab tak wo computer ka no nahi match ho jata hai tb tk guess change hota hai.)

# Second Way ----
comp = random.randint(1,10)
tries = 0
while True:
    guess = int(input("Enter Your Guess : "))

    if guess == comp:
        print(f"You Guess the Right No In {tries} tries")
        tries += 1
        break
    elif guess > comp:
        print("You Guess Higher No")
        tries += 1
    elif guess < comp:
        print("You Guess Lower No")
        tries += 1


# Q4 End