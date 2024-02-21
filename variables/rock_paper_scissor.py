import random
mylist = ['rock','paper','scissor']
z=random.choice(mylist)
while(True):
    choice = input("Enter your choice : ")
    print("computer choosed "+z)
    if((choice=="rock" and z == "paper") or (choice == "scissor" and z == "rock")
    or (choice == "paper" and z=="scissor")):
        print("Computer wins!!")
    elif(choice==z):
        print("Draw!!")
    else:
        print("You wins!!")
    
    play_again = input("Play Again (yes/no):  ").lower()
    if play_again != 'yes':
        break
    
print("Bye")