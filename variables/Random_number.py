import random

# x = random.randint(1,6)
# print(x) # random number b/w 1 to 6

# y=random.random()
# print(y) # random number between 0 to 1


# rock paper and scissor using python

# mylist = ['rock','paper','scissor']
# z=random.choice(mylist)

# choice = input("Enter your choice : ")
# print("computer choosed "+z)
# if((choice=="rock" and z == "paper") or (choice == "scissor" and z == "rock")
#    or (choice == "paper" and z=="scissor")):
#     print("Computer wins!!")
# elif(choice==z):
#     print("Draw!!")
# else:
#     print("You wins!!")

#----shuffle keyword

cards = [1,2,3,4,5,6,7,8,9,"Q","K","J","A"]
random.shuffle(cards)
print(cards)