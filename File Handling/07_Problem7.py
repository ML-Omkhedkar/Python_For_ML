
# with open("log.txt") as f:
#     lines = f.readlines()

# lineno = 1

# for line in lines:
#     if "python" in line:
#         print(f"Yes Python is Present in line no {lineno}")
#         break
#     lineno += 1    

# else:
#     print("No Python Is Not Prensent")    




with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "omkar" in line:
        print(f"Yaa Omkar is Here Line NO {lineno}")   
        break
    lineno += 1
else:
    print(" Noo This type of anyword is not Prensent in this file ")     




























