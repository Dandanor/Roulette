import random
arr= [*range(1,37),'0','00']

spin=random.choice(arr)
x=int(input("enter your bet "))
if x==spin:
    print (f"the winning number is {spin}, you win")
else:
    print (f"the winning number is {spin}, you lose")
