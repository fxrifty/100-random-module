import random as r
def cards():

 suit=["Diamonds","Spades","Clubs","Hearts"]
 chosen=r.choice(suit)
 card=["Ace","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
 chosen1=r.choice(card)

 print(chosen1,"Of",chosen)

print("PLAYER 1'S CARDS")
for i in range(5):  
 cards()

print("")
print("PLAYER 2'S CARDS")
for i in range(5):  
 cards()