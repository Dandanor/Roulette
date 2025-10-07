def get_color(roulette):
    if isinstance(roulette,str):
        return "Green"
    if isinstance(roulette,int):
        if roulette%2==0:
            return "Black"
        else:
            return "Red"
#returns the winning color