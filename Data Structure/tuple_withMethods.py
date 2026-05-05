t = (1,2,34,5,6,7,5,34,7,4,7,8,7) # Tuple is haterogenous We Can Add Multiple Data Types
print(t) # printing tuple

# t[2] = 39 # TypeError : Tuple mai hum Value Ko change nhi krr sakte tuple is inmutable

# Tuple Methods............

index = t.index(34) # Finds The Frist Occurrence of 34 (pahila 34 kitane index pe ata hai bata dega)
print(index)

count = t.count(7) # Count Occurrences of 7 (tuple mai 7 kitani bar hai wo bata dega ye method)
print(count)
