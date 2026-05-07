

### 10. FizzBuzz (Classic but Powerful)

# **Question:** 1 se 50 tak print kar:

# * 3 se divisible → "Fizz"
# * 5 se divisible → "Buzz"
# * dono se → "FizzBuzz"

# **Samjha:**
# Ye question tera logic aur condition handling strong karega

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Bizz")

