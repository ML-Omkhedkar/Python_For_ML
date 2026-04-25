
a = 12
b = 12

# and --> Return True if both condition are True

# all conditions are the true so output is True
print(a == b and 50 == 50 and 1 == 1 and 2 != 1)

# this time im add a false contion a !=b so output is False this time
print(a != b and 50 == 50 and 1 == 1 and 2 != 1)

# or --> Return True if at least one condition is True

# Prints the True Becase 12 == 12 and 1==1 is true condition
print(a != b or 12 == 12 or 1 == 1)

# Prints the False because this time all contions are False
print(a != b or 13 == 12 or 5 == 1)

# not --> Reverse the boolean value

# prints the False Because Value is true
print(not True)
print(not a == b) # this is aloso false because a and b is also equal (true)

# Prints the true beause value is False
print(not False)
print(not a != b) # This is returns True Because a!=b condition is False