import random as r
def suits():
 suit=["Diamonds","Spades","Clubs","Hearts"]
 chosen=r.choice(suit)
 print(chosen)
def cards():
 card=["Ace","1","2","3","5","6","7","8","9","10","Jack","Queen","King"]
 chosen=r.choice(card)
 print(chosen)

def hand():
    cards(),print("Of"),suits()
   
    



hand()