def betnumber (spin,balance,color,betamount):
    while True:
        try:
            y=int(input("enter your bet (number) "))
            if y==spin:
                print (f"you win! the winning number is {spin} , and the color is {color} ")
                balance+=betamount*36
            else:
                print (f"you lose, the winning number is {spin} , and the color is {color} ")
            return balance
        except ValueError:
            print ("Please enter an Integer")

#number betting function
