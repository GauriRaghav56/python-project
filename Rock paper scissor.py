import random
again = "yes"
while again == "yes":
    choices =  ["rock","paper","scissors"]
    user = input("Rock,Paper ya Scissor:").lower()
    computer = random.choice(choices)
    print("computer:",computer)
    if user == computer:
        print("Match Draw")
    elif(user == "rock" and computer == "scissors")or\
        (user == "paper" and computer =="rock")or\
        (user == "scissors" and computer == "paper"):
       print("you Win!")
    else:
       print ("computer Wins")
    again = input(" kya app dubara khelna chhate hain?(yes/no):").lower()
print("Thank you for plaing")