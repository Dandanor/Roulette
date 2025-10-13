def get_color(roulette):
    red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    if isinstance(roulette,str):
        return "Green"
    if isinstance(roulette,int):
        if roulette in red:
            return "Red"
        else:
            return "Black"
#returns the winning color