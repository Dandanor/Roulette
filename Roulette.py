import random, bet,betcolor,betnumber,betrange
from color import get_color
arr= [*range(1,37),'0','00']
balance=50
while balance>0:

    spin=random.choice(arr)
    betstyle=input("enter your betting preferance (Color,Number,Range) ").capitalize()
    betamount=bet.betting(balance)
    color=get_color(spin)

    if betstyle=="Color":
        balance=betcolor.betcolor(spin,color,betamount,balance)
    elif betstyle=="Number":
        betnumber.betnumber(spin,balance,color,betamount)
    elif betstyle=="Range":
        betrange.betrange(spin,balance,betamount,color)
    balance-=betamount
    print (f"current balance is {balance}")
print ("Game Over!")
            
            
