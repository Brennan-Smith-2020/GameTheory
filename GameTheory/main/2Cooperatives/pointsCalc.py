def pointCalc(move1, move2, move3, move4, move5, move6, p1points, p2points, p3points, p4points, p5points, p6points, player1name, player2name, player3name, player4name, player5name, player6name):
    if move1 == 'D' and move2 == 'C':
        p1points += 5
    elif move1 == 'C' and move2 == 'D':
        p2points += 5
    elif move1 == 'C' and move2 == 'C':
        p1points += 3
        p2points += 3
    elif move1 == "D" and move2 == "D":
        p1points -= 3
        p2points -= 3

    if move6 == 'D' and move2 == 'C':
        p5points += 5
    elif move6 == 'C' and move2 == 'D':
        p6points += 5
    elif move6 == 'C' and move2 == 'C':
        p5points += 5
        p6points += 5
    elif move6 == "D" and move2 == "D":
        p5points -= 5
        p6points -= 5

    # Considering Lana's moves
    if move1 == 'D' and move3 == 'C':
        p3points += 5
    elif move1 == 'C' and move3 == 'D':
        p4points += 5
    elif move1 == 'C' and move3 == 'C':
        p3points += 3
        p4points += 3
    elif move1 == "D" and move3 == "D":
        p3points -= 1
        p4points -= 1

    # Considering Ray's moves
    if move1 == 'D' and move4 == 'C':
        p4points += 5
    elif move1 == 'C' and move4 == 'D':
        p5points += 5
    elif move1 == 'C' and move4 == 'C':
        p4points += 5
        p5points += 5
    elif move1 == "D" and move4 == "D":
        p4points -= 3
        p5points -= 3

    # Considering Forlot's moves
    if move1 == 'D' and move5 == 'C':
        p5points += 5
    elif move1 == 'C' and move5 == 'D':
        p5points += 5
    elif move1 == 'C' and move5 == 'C':
        p5points += 3
        p6points += 3
    elif move1 == "D" and move5 == "D":
        p5points -= 3
        p6points -= 3

    print(f"Player 1: ({player1name})   {p1points}        Player 2:  ({player2name})   {p2points} \n Player 3: ({player3name}),   {p3points}  Player 4: ({player4name}),   {p4points}  Player 5: ({player5name}),   {p5points}  Player 6: ({player6name}),   {p6points}")
    return p1points, p2points, p3points, p4points, p5points, p6points
# Everyone fights their player-1