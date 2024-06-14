import random as r
def strenth():
    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice3=r.randint(1,6)
    dice4=r.randint(1,6)
    total=[dice1,dice2,dice3,dice4]
    total.remove(min(total))
    strength=(sum(total))
    print("Your Strength Is",strength)
    
def wisdom():
    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice3=r.randint(1,6)
    dice4=r.randint(1,6)
    total=[dice1,dice2,dice3,dice4]
    total.remove(min(total))
    wisdom=(sum(total))
    print("Your Wisdom Is",wisdom)

def dexterity():
    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice3=r.randint(1,6)
    dice4=r.randint(1,6)
    total=[dice1,dice2,dice3,dice4]
    total.remove(min(total))
    dexterity=(sum(total))
    print("Your Dexterity Is",dexterity)

def charisma():
    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice3=r.randint(1,6)
    dice4=r.randint(1,6)
    total=[dice1,dice2,dice3,dice4]
    total.remove(min(total))
    charisma=(sum(total))
    print("Your Charisma Is",charisma)

def constatution():
    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice3=r.randint(1,6)
    dice4=r.randint(1,6)
    total=[dice1,dice2,dice3,dice4]
    total.remove(min(total))
    constatution=(sum(total))
    print("Your Constatution Is",constatution)

def intt():
    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice3=r.randint(1,6)
    dice4=r.randint(1,6)
    total=[dice1,dice2,dice3,dice4]
    total.remove(min(total))
    intt=(sum(total))
    print("Your Intelligence Is",intt)

strenth()
dexterity()
constatution()
intt()
wisdom()
charisma()