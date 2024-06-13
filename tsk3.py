import random as r

while True:
 user=input("Enter Your Choice rock, paper or scissors: ")
 choices=["rock", "paper", "scissors"]
 ai=r.choice(choices)
 print(f"Your Choice Was {user}, The Computer Chose {ai} \n")
 break

if user == ai:
    print(f"Both Players Selected {user}\n")
elif user == "rock":
    if ai == "scissors":
        print("Rock Smashes Scissors \nYou Win\n")
    else:
        print("Paper Covers Rock \nYou Lose\n")
elif user == "paper":
    if ai == "rock":
        print("Paper Covers Rock \nYou Win\n")
    else:
        print("Scissors Cuts Paper \nYou Lose\n")
elif user == "scissors":
    if ai == "paper":
        print("Scissors Cuts Paper \nYou Win\n")
    else:
        print("Rock Smashes Scissors \nYou Lose\n")
