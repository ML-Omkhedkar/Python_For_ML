# Q1. Accept two numbers and print the greatest between them.

from ast import For
from _sitebuiltins import _Printer
from string import ascii_lowercase
a = 10
b = 20

# Condition Is Kya 10, 20 se Bada hai kya ?
if a > b:
    print("A Is Big") # Contion is False So Program Prints Else
else:
    print("B Is Big")

# Same Output But Contion IS Changed
if a < b:
    print("B Is Big") # Contion is True So Program Prints This
else:
    print("A Is Big")  

# End Of 1st Q

# Q2. Accept the gender from the user as char and print the respective greeting message 

Gender = input("Enter Your Gender Male Or Female: ")

# if "Male" in Gender or "M" in Gender:
#     print("Good Morning Sir") # If User Input Male Ya M To Ye Print Hoga
# elif "Female" in Gender or "F" in Gender:
#     print("Good Morning Mam") # If User Input Female Ya F To Ye Print Hoga
# else:
#     print("Please Enter The Valid Gender") # Agar User Kuch Bhi (Invalid) Input Deta hai To Ye Print Hoga

# Im Tring Anoter Method to Print The Same Result

if Gender == "Male" or Gender == "M":
    print("Good Morning sir")

elif Gender == "Female" or Gender == "F":
    print("Good Morning Mam")

else:
    print('Please Enter Valid Gender') 

# Second Q Is End   

# Accept an integer and check whether it is an even number or odd.

# n = 10

# Im Getting Input From User For Make Program Better
n = int(input("Enter A No To check it is even Or Odd: "))

if n%2 == 0:   # 
    print(f"{n} Is Even")

elif n%2 != 0: # Yahan Par % Ka Meaning Hai Remainder Yaani Ke Baki  
    print(f"{n} Is Odd No")

# Mai Elif Ki jagh Seedha Use Krr Sakta hu But Mai Islie Use Karra hu Taake Program Ko Clean Rakhe

# End Of Third Q

# Q4. Accept name and age from the user. Check if the user is a valid voter or not.

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

if age >= 18:
    print(f"{name} You Are elegible For Voting")

else:
    print(f"{name} You Are Not Elegible For Voting")

# End Of Fourth Q

# Q5. Accept a year and check if it a leap year or not

year = int(input("Enter A Year: "))

# (Year % 400 == 0) -> Exception

#this is My Vesion but ChatGPT Suggest me a Better Version
# if year%4 == 0:
#     print("Leap Year")

# else:
#     print("Not Leap Year")

# Chatgpt Vesion Is
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# End Of Fifth Q

