s = {1,2,3,4,5,5,5,8,9,0} # Set is semi-heterogenous
print(s) # prints in order (set is unorderd hmm usse index se acces nhi krr sakte)
# set dublicates values store nhi karta and srt is mutable hmm values change krr sakte hai but index se nhi medhods se

# print(s[0]) #TypeError: 'set' object is not subscriptable (hmm index se isse acces nhi krr sakte)

# Set Some Methods........
s.add(6) # adds An element to the Set ( hmm Element ko set mai add krr saktr hai set() se)
print(s) # Priting updated Set with 6

s.remove(5) # removes 5 (KeyError: agr nhi mila to error throw hoga....) 
print(s) # printing updated set without 5

s.discard(7) # removes 7 (but ise set mai 7 nhi mila to bhi error nhi dega ye)
print(s) # printing set without 7 agr 7 nhi mila tab bhi normaly set print krr dega without error

# pop_element = s.pop() # removes random elements
# print(pop_element)

s.clear() # Removes All Elements
print(s) # prints Empty Set : set()

#====================================================

a ={1,2,3,4}
b = {4,5,6,7,8}

# union_set = a.union(b)
# print(union_set)
# # Sorcut way
# print(a|b)

# intersection_set = a.intersection(b)
# print(intersection_set)
# # Shortcut Way to print
# print(a&b)

# set_diffrence = a.difference(b)
# print(set_diffrence)
# # Shortcut Way to print
# print(a-b)

symmetric_deff = a.symmetric_difference(b)
print(symmetric_deff)
# Shortcut Way to print
print(a^b)