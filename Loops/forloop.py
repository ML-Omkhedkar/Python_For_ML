
# range(start , stop , step)

for i in range(1 , 21 , 2):
    print(i)


# Default Start and Step Value are 0 and 1 respectively

# for i in range(21):
#      print(i)

# You Can Write Like this also

# a = range(21)
# for i in a:
#     print(i)

# Print the numbers from 50 to 1 reverse order start from 50 and stop at 1 and step by -1
# for i in range(50,0,-1):
#     print(i)

# you can also use for lop for printing negative numbers

# for i in range(-1 , -16, -1):
#     print(i)

# nasted for loop this loop prints pattern of numbers

# for i in range(5):
#     for j in range(1, i+1):
#         print(j , end=" ")
#     print(i)    

# for loop with break and else

# for i in range(1, 11):``
#     if i == 5:
#         break
#     print(i)
# else:
#     print("loop completed")

# For Loop With Cotinue and else

for i in range(1, 21,1):
    if i == 11:
        continue
    print(i)
else:
    print("Loop Compited !")

# Printing Sring using For loop without indexing

str = "Omkar Khedkar"

# for i in str:
#     print(i)

for i in range(5): # print only "omkar" using index
    print(str[i])

for i in range(len(str)): # printing the string using len function  
    print(str[i])