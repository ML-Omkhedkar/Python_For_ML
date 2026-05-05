# class employee:
#     company = "Microsoft"
#     sallery = 120000
#     language = "Python"

# Omkar = employee()
# Omkar.name = "omkar"
# print(Omkar.name , Omkar.sallery, Omkar.company,  Omkar.language )

# shubham = employee()
# shubham.name = "shubham"
# print(shubham.name , shubham.sallery, shubham.company,  shubham.language)
# harry = employee()
# harry.name = "harry"
# print(harry.name , harry.sallery, harry.company,  harry.language )

# om = employee()
# om.name = "om"
# print(om.name , om.sallery, om.company,  om.language )





class Employee:
    company = "Microsoft"

    def __init__(self, name, salery, pin):
        self.name = name
        self.salery = salery
        self.pin = pin

e1 = Employee("Omkar", 100000,  414113)
print(e1.name, e1.salery, e1.pin)

e2 = Employee("Harry", 100000,  56587)
print(e2.name, e2.salery, e2.pin)

e3 = Employee("Shubham", 900000,  322353)
print(e3.name, e3.salery, e3.pin)

e4 = Employee("Yash", 100000,  675823)
print(e4.name, e4.salery, e4.pin)



