# ### 1. Even / Odd Check

# **Question:** Ek number input le aur check kar ki wo even hai ya odd.
# **Samjha:**
# Agar number 2 se perfectly divide ho jaye → even
# warna → odd
# 👉 Hint: `%` operator use kar

# Error Handling maine add ki hai just for practice or invalid input 

# try:
#     num = int(input("Enter No To Check Its Even or Odd: "))
#     if num%2 == 0:
#         print("its even No")
#     else:
#         print("its Odd No")    

# except:
#     print("Somthing Wrong....!") 

# =============================================================

# **Question:** List me se sabse bada number find kar
# **Example:** `[3, 7, 2, 9, 5] → 9`
# **Samjha:**
# Har element compare kar, ek variable me current max store kar

# maine yaha samalest finding ka bhi logic try kiya hai and its working good

# l = [2,3,4,5,5,8,9,11]
# largest = 0
# smallest = 0
# for i in range(len(l)): # for itretion all list elements
#     if l[i] > l[i+-1]: # for Finding Gretest No
#         largest = l[i]

#     elif l[i] < l[i+-1]: # for Finding Smallest No
#         smallest = l[i]

# print(f"Largest No In List is {largest} And Smallest No Is {smallest}")

# =============================================================
### 3. Reverse a String

# **Question:** Ek string ko reverse kar
# **Example:** `"hello" → "olleh"`
# **Samjha:**
# Last se start karke new string bana ya slicing use kar

str = "omkar Builds"

# rev = str[::-1]
# print(rev)

# Using For Loop

# for rev in range(len(str)-1 ,-1, -1): 
#     print(str[rev], end = "") # end isi liye lagaya hai kyuki hame hrr letter ek new line mai mil rha tha ent se wo ek hi line mai print hoga

# =============================================================

### 4. Count Vowels

# **Question:** String me kitne vowels () hai count kar
# **Samjha:**
# Loop chala aur check kar har character vowel hai ya nahi

# str = "omkar Builds"
# v_letters = "aeiou"
# vowel = 0
# for v in str:
#     for ch in v_letters:
#         if ch in v:
#             print(ch)
#             vowel+=1
# print(f"vowel count: {vowel}")

# chatgpt se madat li to usne simply ye code bataya hai its easy
# but i did not understand it corectly yet 
# but i know now 

# str = "omkar Builds"
# v_letters = "aeiou"
# count = 0

# for v in str:
#     if v.lower() in v_letters:
#         count += 1

# print(count)

# ==============================================================
# this is the challage quetion for me given by from ChatGpt
# jismai mujhe ye print karn ahai ki vowel charecter kitni bar aya hai str mai 

# str = "Education"
# dict = {}

# for ch in str:
#     if ch.lower() in "aeiou":
#         if ch.lower() in dict:
#             dict[ch] += 1
#         else:
#             dict[ch] = 1

# print(dict)    

# again same

# str = "omkar Builds"
# freq = {} # Empty Dict
# v_letters = "aeiou"
# for ch in str:
#     if ch in v_letters:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1    
# print(freq)

# ==============================================================

# ### 5. Palindrome Check

# **Question:** Check kar string palindrome hai ya nahi
# **Example:** `"madam" → Yes`, `"hello" → No`
# **Samjha:**
# Original string == reverse string → palindrome

pal = "madamm"
rev = pal[::-1]

if pal == rev:
    print("Yes Your string IS palindrome")
else:
    print("No Your String Is not palindrome")

#==========================================================

### 6. Frequency of Elements

# **Question:** List me har element kitni baar aaya count kar
# **Example:** `[1,2,2,3,1] → {1:2, 2:2, 3:1}`
# **Samjha:**
# Dictionary use kar, key = element, value = count

# l = [1,2,3,4,5,5,6,6,9]
# dup_dict = {}

# for n in l:
#     if n in dup_dict:
#         dup_dict[n] += 1
#     else:
#         dup_dict[n] = 1

# print(dup_dict)    

#==========================================================

# ### 7. Sum of Digits

# **Question:** Ek number ke digits ka sum nikal
# **Example:** `123 → 1+2+3 = 6`
# **Samjha:**
# String me convert karke ya `%` aur `//` se tod sakta hai


num = [1,2,3,4,5]

for n in num:
    sum_ofn = n + n + 1
    
print(f"Your ans Is {sum_ofn}")

#==========================================================


# ### 8. Find Duplicates

# **Question:** List me kaunse elements duplicate hai wo nikal
# **Example:** `[1,2,2,3,4,4] → [2,4]`
# **Samjha:**
# Ek `seen` set aur ek `duplicate` list bana — agar element already seen me hai → duplicate

l = [1,2,3,4,5,4,3,]

seen = set()
duplicates = set() # Set use kar rahe hain taaki duplicate khud repeat na ho
for x in l:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(seen)
print(duplicates)

### 9. Second Largest Number

# **Question:** List ka second largest number find kar
# **Example:** `[10, 20, 5, 8] → 10`
# **Samjha:**
# Sort kar ya manually 2 variables maintain kar (max & second max)


l = [1,2,3,7,8,11,55,66]
largest = 0
second_largest = 0

for n in l:
    if n > largest:
        # Before updating largest, move the old largest to second_largest
        second_largest = largest
        largest = n
    elif n < second_largest and n != largest:
        # If n is not the biggest but bigger than our current second
        second_largest = n

print(f"Largest: {largest}")   
print(f"Second Largest: {second_largest}")