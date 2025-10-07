import random, bet,betcolor
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
        y=int(input("enter your bet (number) "))
        if y==spin:
            print (f"you win! the winning number is {spin} , and the color is {color} ")
            balance+=betamount*36
        else:
            print (f"you lose, the winning number is {spin} , and the color is {color} ")
    elif betstyle=="Range":
        myrange=input("enter your desired range (1-18 or 19-36) ")
        if myrange=="1-18":
            if spin<=18:
                print (f"you win, the winning number is {spin} , and the color is {color} ")
                balance+=betamount*2
            else:
                print (f"you lose, the winning number is {spin} , and the color is {color} ")
        elif myrange=="19-36":
            if spin>=18:
                print (f"you win, the winning number is {spin} , and the color is {color} ")
                balance+=betamount*2
            else:
                print (f"you lose, the winning number is {spin} , and the color is {color} ")
        else:
            print ("invalid range, please try again")
    balance-=betamount
    print (f"current balance is {balance}")
print ("Game Over!")
            
            
