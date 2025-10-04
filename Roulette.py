import random
arr= [*range(1,37),'0','00']

spin=random.choice(arr)
x=input("enter your bet ").capitalize()

if x=="Red" and spin%2==1:
    print (f"the winning number is {spin}, you win")
elif x=="Black" and spin%2==0:
    print (f"the winning number is {spin}, you win")
elif x=="Green" and (spin=='0' or spin=='00'):
    print (f"the winning number is {spin}, you win")
else:
    print (f"the winning number is {spin}, you lose")
