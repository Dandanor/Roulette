def betrange (spin,balance,betamount,color):
    while True:
        try:
            myrange=input("enter your desired range (1-18 or 19-36) ")
            if myrange=="1-18":
                if spin<=18:
                    print (f"you win, the winning number is {spin} , and the color is {color} ")
                    balance+=betamount*2
                else:
                    print (f"you lose, the winning number is {spin} , and the color is {color} ")
                return balance
            elif myrange=="19-36":
                if spin>=18:
                    print (f"you win, the winning number is {spin} , and the color is {color} ")
                    balance+=betamount*2
                else:
                    print (f"you lose, the winning number is {spin} , and the color is {color} ")
                return balance
            else:
                raise ValueError("please enter a valid range")
        except ValueError as e:
            print (e)

if __name__=="__main__":
    betrange(14,50,50,"black")