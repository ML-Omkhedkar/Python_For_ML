def pattern(n):
    if n==0:
        return

    print("*" * n)
    pattern(n-1)

pattern(5)
print("")

def pattern2(n):
    if n==0:
        return

    print("*" * n)    
    pattern(n-1)

pattern2(7)       