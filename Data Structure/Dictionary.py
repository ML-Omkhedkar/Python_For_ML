# Dictionary syntax and working
Dict= {"name" : "omkar", #dict is mutable you can change add remove, and also dublicates are alowed in dict but only values not keys
    "age" : 22,
    "language" : "Python",
    "intrest" : "ML"
    }

print(Dict["name"], Dict["intrest"], Dict["language"]) # Output: omkar ML Python

# Dictionary traversing
numbers = {1:10, 2:20, 3:30, 4:40, 5:50}

for i in numbers:
    print(i, ":", numbers[i])