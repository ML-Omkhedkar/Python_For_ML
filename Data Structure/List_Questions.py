# Q1. Print positive and negative elements of an List

from sys import set_coroutine_origin_tracking_depth
l = [1,2,3,-2,-4,5,-1]

positive = []
negative = []
for i in l:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print(positive) # Positive Numbers
print(negative) # Negative Numbers
# Q1 End
# ==============================================
# Q2. Mean of List elements

l2 = [1,2,3,4,5,6,7] 
# Initialize variables
sum = 0 
count = 0
# Loop through the list
for num in l2:
    sum = sum + num # accumerate sum
    count = count + 1 # count element

# Calculate mean
mean = (sum/count) # total sum / Count 
print(mean)

# second and easy way (mujhe abhi abhi pata chala jab maine search kiya tha copilot pe)---

# mean = sum(l2)/len(l2) # sum of list elements / Number of Elements In List
# print(mean) # Mean Of List Elements
 
# Q2 End

# ==============================================

# Q3. Find the greatest element and print its index too

# l3 = [12,33,4,5,65,66,345]
# max_value = l3[0]
# max_index = 0

# for i in range(len(l3)):
#     if l3[i] > max_value:
#         max_value = l3[i]
#         max_index = i

# print("Greatest Element In List : ", max_value) # Printing Greatest Element
# print("Greatest Element Index : ", max_index) # Printing Index of Greatest Element

# i need more practice of this Type of Questions honestly ----- 

# l = [123,45,664,7,6756,342,1]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"the largest no is {largest} at index {index}")

# second way to find the greatest element from the list (only)

# print(max(l)) # print the greatest element from the list
# print(l.index(max(l))) # and uss ka index bhi print krega (first occur)

# Q3 end 
# ==============================================
# Q4 Find the second greatest element with indexes 

l = [123,45,664,7,6756,342,1,765]

gretest = l[0]
s_gre = l[0]
index = 0
s_index = 0

for i in range(len(l)):
    if l[i] > gretest:
        s_gre = gretest
        s_index = index
        gretest = l[i]
        index = i
    elif l[i] > s_gre:
        s_gre = l[i]
        s_index = i
print(f"The gretest no is {gretest} at index {index} and second gretest no is {s_gre} at index {s_index}")
# Q4 End

# ==============================================
# Q5. Check if List is sorted or not.

l = [12,13,14,15,16]
for i in range(len(l)-1): # (minus 1 isi liye likha hai kyuki indexerror aa rha hai tha out off range kyuki hamara if condition i+1 le rha hai to wo last wale index mai bhi +1 dund rha hai )
    if l[i] < l[i+1]: # agr list ke 0 index se index 1 bada hai to continue hoga
        continue
    else:
        print("Your List is Not Sorted")
        break # if condition false huye to hmm break karenge....
else:
    print("Your List Is Sorted")

# Q5 End
# ==============================================
