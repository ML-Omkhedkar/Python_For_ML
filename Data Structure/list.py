# Yu Can Store Anything in list Like Str, Int, Functions, Bool
l = [12, 44, 234, "omkar" ,5, 45 ,True , 523] # list is haterogenous 

print(l) # Printing List

# You Can Print Specific with Index

print(l[0]) # print 12

#list Slicing same str slicing

print(l[0:4]) # Output: 12, 44, 234, "omkar" 

# you can Start Stop And Step As well 

print(l[0:7:2]) # OutPut: [12, 234, 5, True]

# List With for Loop

l2 = [12, 44, 234, "omkar" ,5, 45 ,True , 523, "shubham", 111]

# for i in l2:
#     print(i)    #Printing l2 Using Simple for Loop

l2[0] = 222 # Mutable --> Mutability refers to whether an object's value can be changed after creation. And List allows this
print(l2)

l3 = [12, 44, 234,12,12,44,3,43,4,12] # Dublicates Are Alowed in List
print(l3)

print(l3[3]) # Ordered --> list ko index se access kr sakte hai.
# List maintains ordered data structure maintains 
# the sequence of elements as they were inserted. This 
# means you can access elements using their position 
# (index)

