# Q. calculate the sum of first n natural numbers.

def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n


print(sum(1))
print(sum(2))
print(sum(3))
print(sum(4))