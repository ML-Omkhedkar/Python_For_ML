print("Start.....")

try:
    a=10
    b= int(input("Enter a number: "))
    c=a/b
    print("The division of a and b is:",c)
except ZeroDivisionError:
    print("Division by Zero is not possible")
finally:
    print("End.....")

# try and else syntax examples

try:
    x= int(input("Enter a number: "))
    if x<0:
        raise ValueError("The number is negative")
    else:
        print("The number is positive")
except ValueError as e:
    print(e)

