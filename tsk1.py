import random as r


ra=r.randint(1,100)
guess=int()
while ra!=guess:
    guess=int(input("Enter A Number: "))
    if guess < ra:
        print("Too Low")
    if guess > ra:
            print("Too High") 
    if guess==ra:
         print("Correct!")
      

        