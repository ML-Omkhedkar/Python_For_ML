# This is a multi If elif Ladder 
# Abhi mere dimag mai idea nhi ki mai kya banau isse so maine pass krr diya hai

if 2>1:
    if 10 > 20:
        pass
    elif 20 > 30:
        pass
    elif 30 < 40:
        pass
    else:
        pass
else:
    pass




temp = int(input("Enter Temprature: "))

# also this is a if elif ladder

if temp <= 0:
    print("Freezing Cold")
elif temp > 0 and temp < 10:
    print("Verry Cold")
elif temp > 10 and temp < 20:
     print("Cold")
elif temp > 20 and temp < 30:
    print("Pleasant")
elif temp > 30 and temp < 40:
    print("Hot")
else:
    print("Temprature Is Verry Hot")

