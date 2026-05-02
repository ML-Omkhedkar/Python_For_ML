l = [22, 33, 45, "om",31, 7,22, "omkar" ]

# l.append("khedkar") # adds 'khedkar' to the end 
# print(l) 

# l.insert(0, 11) # insert 11 at index 0 (0 index ko replace nhi karega bss uss index pe add ho ga and pahile wala agehe wale index pe shift ho jayega )
# print(l) # output: [11, 22, 33, 45, 'om', 31, 7, 'omkar']

# l.extend(1,2,3) # TypeError: list.extend() takes exactly one argument (3 given)[# yaha pe maine ek galti ki jisse muhe TypeError mila and wo hai Bracket [ ] na lagana
# l.extend([1,2,3]) # adds Multiple Items at the end -- multiple items add krr sakte hai hmm isse but end mai
# print(l)

# l.remove(22) # list mai se pahila 22  remove krr dega ye -- removes the frist occurrence of 22 
# print(l) 

# popped_item = l.pop(2) # Removes and stored element at index 2 -- index pe jo bhi value hai (at this time 45 is the value) usse remove karke varible mai store krta hai
# print(popped_item) # printing stored index 2 value (45)
# print(l) # Printing List Without 2 index value (45)

# index = l.index("omkar") # 'omkar' ka index value bata dega ye
# print(index) #  hmne index name ke variable mai "omkar" ka index value store karke print kiya hai Output Is 7 (because 'omkar' at index 7)

# count = l.count("22") # Count Occurences of 22
# print(count) # pahile 22 ka index print karega ye hamare list mai frist 0 index no pe and second 6 index no pe hai 22, so yaha frist wala yani 0 index print hoga...

intL = [5,4,6,3,1,2]
strL = ["omkar", "om", "khedkar" "kuch bhi"]

# l.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
# print(l) # hamare list mai abhi intger bhi and strings bhi so ye function error trow krr rha hai(matlab hamare list mai koi ek hi data type hona chaiye )

# intL.sort() # ye hamare list ko Assending Order mai sort krr dega like 1 2 3....(sort the list in assending order)
# print(intL)

# strL.sort() # with str list is working perfect
# print(strL)

# intL.reverse() # revers the list (list ko ulta matlab revers karke print krega like 6 5 4 3..)
# print(intL)

new_intL = intL.copy() # Hamare intL list ko copy banayega ( cretes a copy of list)
print(new_intL)

intL.clear() # Removes All The Elements From The List (list mai se sab items element ko remove krr dega ye)
print(intL) # Print Empty list Because of .clear() function