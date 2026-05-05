import random

# def game():
#     print("You Are the playing game....")
#     score = random.randint(1, 80)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()

#         if (hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0   

#     print(f"your Score: {score}")
#     if (score > hiscore):
#       with open("hiscore.txt", "w") as f:
#        f.write(str(score))

#     return score

# game()





# def game2():
#     print("You Are The Playing Game 2.....")
#     score = random.randint(1 , 66)
#     with open("hiscore2.txt") as h:
#         hiscore = h.read()

#         if hiscore != "":
#             hiscore = int(hiscore)

#         else:
#             hiscore = 0

#     print(f" Your Score: {score}")

#     if (score > hiscore):
#         with open("hiscore2.txt" , "w") as h:
#             h.write(str(score))

#     return score
# game2()




def game3():
    print("You Are the playing game 3........")
    score = random.randint(1, 88)

    with open("hiscore3.txt" , "r") as f:
        hiscore = f.read()

        if hiscore != "" :
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score: {score}")

    if (score > hiscore):
        with open("hiscore3.txt" , "w") as f:
            f.write(str(score))
    return score        

game3()

