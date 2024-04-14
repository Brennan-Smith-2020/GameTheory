# Put this func in whatever charecter you want to move first
moved = False
def GoFirst(MOVE):
    global moved
    if moved == False:
        moved = True
        move = MOVE
        return move

