a = 111
b = 22
c = 34

def grettest(a,b,c):
   if a>b and a>c:
    print(f"a {a} is greter") 
   elif b>a and b>c:
    print(f"b {b} is greter") 
   else:
    print(f"c {c} is greter") 

grettest(a,b,c)