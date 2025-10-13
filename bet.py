def betting(Balance):
    while True:
        try:
            bet=int(input("enter your bet amount: "))
            if bet>Balance:
                print ("invalid bet amount, please enter a valid amount")
            else:
                return bet
        except ValueError:
            print ("please enter an integer")
#amount betting function