strategy_name = "beat the most frequent move"

def move(my_history, their_history):
    if len(my_history) == 0:
        return "p"

    r_list = []
    p_list = []
    s_list = []

#keep track of opponent's moves by adding each move to a specific list

    for opponentterriblemove in their_history:
        if opponentterriblemove == "r":
             r_list.append("r")
        elif opponentterriblemove == "p":
             p_list.append("p")
        elif opponentterriblemove == "s":
             s_list.append("s")

#count total # of moves and save it as total
#then cross-check it with each list and if one list has more than 1/2 or 50% of all moves, counter

    total = len(their_history)

    if len(r_list) > total * 0.5:
         return "p"
    elif len(p_list) > total * 0.5:
         return "s"
    elif len(s_list) > total * 0.5:
        return "r"
#mylastmove is what we played last, and its hardcoded so that it gets some wins in case something fails
    else:
        mylastmove = my_history[-1]
        if mylastmove == "r":
            return "s"
        elif mylastmove == "s":
            return "p"
        else:
            return "r"
