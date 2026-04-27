# Q1. Accept an integer and Print hello world n times

# n = int(input("Enter No: "))
# h = "Wollo Word"

# for i in range(n):
#     print(h)

# Q1 End

# Q2. Reverse for loop. Print n to 1

# n = int(input("Enter No: "))

# for i in range(n,1,-1):
#     print(i)

# Q2 End

#Q3 Take a number as input and print its table

# frist Simple way to print table of n

# n = int(input("Enter No to get table: "))
# for i in range(n,(n*10)+1 , n):
#     print(i)

# Second Way To Print Table and  I Like Second Method Because its Logical and clean to understand

# t = int(input(" Enter no to Print Table: "))
# for i in range(1 , 11):
#     print(f"{t} X {i} = {t*i}")

# Q3 End

# Q4. Sum up to n terms

# n = int(input("Enter The No : "))

# sum = 0
# for i in range(1 , n+1):
#     sum += i
# print(f"Sum is : {sum}")

# Q4 End

# Q5. Factorial of a number

# n = int(input("Enter Your Number "))

# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print(f"Your Factorial is {fact}")

# Q5 End

# Q6. Print the sum of all even & odd numbers in a range separately

# n = int(input("Enter The Range : "))
# even = 0
# odd = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         even += i
#     else:
#         odd += i

# print(f"Your even sum is {even} and odd sum is {odd}")

# Q6 End

#Q7. Print all the factors of a number

# n = int(input(" Enter No: "))

# for i in range(1 , n+1):
#     if n%i == 0:
#         print(f"Factors are: {i}")

# Q7 End

# Q8. Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself 

# n = int(input("Check Your No Is Perfect Or Not: "))
# sum = 0 

# for i in range(1, n):
#     if n%i == 0:
#         sum += i
# print(sum)

# if sum == n:
#     print("Your No Is Perfect")
# else:
#     print("your no Is Not Perfect")
# Q8 End


# Q9 Check wether the number is prime or not

# n = int(input("Enter Your Number To Check its Prime or Not"))
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count += 1

# if count == 2:
#     print("Your Number Is Prime")
# else:
#     print("Your Number Is Not Prime")    

# Q9 End

# Q10. Reverse a string without using in build functions.

# s = "Omkar Khedkar"

# NewS = ""
# # print(len(s))

# for i in range(len(s)-1, -1, -1):
#     print(s[i])
#     NewS = NewS + s[i]
# print(NewS)

# Q10 End

# Q11. Check string is Pallindrome or not
# 
#  
# s = "naman"

# NewS = ""
# # print(len(s))

# for i in range(len(s)-1, -1, -1):
#     print(s[i])
#     NewS = NewS + s[i]

# if NewS == s:
#     print("Your Sring Is Pallindrome")
# else:
#     print("Your Sring Is not Pallindrome")

# Q11. End

# Q12. Count all letters, digits, and special symbols from a given string 

str1 = "P@#yn26at^&i5ve"

letters = 0
digit = 0
special = 0

for i in range(len(str1)):
    if str1[i].isalpha():
        letters += 1
    elif str1[i].isdigit():
        digit += 1
    else:
        special += 1

print(f"Letters: {letters}, Digits: {digit}, Special Symbols: {special}")