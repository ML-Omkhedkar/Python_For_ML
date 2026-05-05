from random import randint

# class Train:

#     def __init__(self, wtf , name, ticket, help):

#         self.wtf = wtf
#         self.name =  name
#         self.ticket = ticket
#         self.help = help

#     @staticmethod
#     def greet():
#         print("Thank You! From Wande Bharat")


# p = Train("mumbai to Delli", "wandhe bharat", randint(244, 555) , 2112)
# print(f"Welcome To {p.name}. You Ticket No Is {p.ticket} And Your Destination is {p.wtf} For Any Help You Can Call {p.help}")
# p.greet()    




class train:

    def __init__(slf, Trainno):
        slf.Trainno = Trainno
        
    def book(self, fro, to):
        print(f"Your Ticket Is Booked On {self.Trainno} Train NO.. For Journey {fro} To {to}")

    def getstatus(self):
        print(f"Train is running on time.")

    def fare(self, fro, to):
        print(f"your {fro} to {to} is Booked and your Train no is {self.Trainno} on seat {randint(66, 555)}")

t = train(12324)

t.book("Pune" , "Mumbai")
t.getstatus()
t.fare("pune", "Mumbai")