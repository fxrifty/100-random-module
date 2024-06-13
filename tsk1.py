import random as r

ra=r.randint(1,100)
print(ra)
guess=int(input("Enter A Number: "))
while ra!=guess:
    if guess < ra:
        print("Too Low")
        guess = int(input("Enter Another Number: "))
        if guess > ra:
            print("Too High") 
            guess = int(input("Enter number again: "))
        if guess==ra:
         print("Correct!")
      

        