import os
from pointsCalc import pointCalc
from firstMove import GoFirst
import matplotlib.pyplot as plt
import random

deflections_ben = 0
deflections_almanac = 0
cCount = 0

def ben(lastMove="C", deflections=0):
    global deflections_ben
    move = GoFirst('C')  # C = cooperate, D = deflect

    if lastMove == 'D':
        deflections_ben += 1
        move = "C"

    if deflections_ben == 2:
        deflections_ben = 0
        move = 'D'
        deflections += 1

    elif deflections_ben > 2:
        move = "C"

    if lastMove == "C":
        move = "C"

    if deflections >= 3:
        move = "C"
    return move

def ben2(lastMove="C", deflections=0):
    global deflections_ben
    move = GoFirst('C')  # C = cooperate, D = deflect

    if lastMove == 'D':
        deflections_ben += 1
        move = "C"

    if deflections_ben == 2:
        deflections_ben = 0
        move = 'D'
        deflections += 1

    elif deflections_ben > 2:
        move = "C"

    if lastMove == "C":
        move = "C"

    if deflections >= 3:
        move = "C"
    return move



def ray(lastMove="C", deflections=0):
    global deflections_ray
    deflections_ray = 0

    if lastMove == 'D':
        deflections_ray += 1
        move = "D"
        deflections += 1

    if deflections_ray == 2:
        deflections_ray = 0
        move = 'C'

    elif deflections_ray > 2:
        move = "D"
        deflections += 1

    if lastMove == "C":
        move = "D"
        deflections += 1

    if deflections >= 3:
        move = "C"
        
    return move

def forlot(lastMove="D", deflections=0):
    global deflections_forlot
    deflections_forlot = 0

    if lastMove == 'D':
        deflections_forlot += 1
        move = "D"
        deflections += 1

    if deflections_forlot == 2:
        deflections_forlot = 0
        move = 'D'
        deflections += 1

    elif deflections_forlot > 2:
        move = "C"

    if lastMove == "C":
        move = "D"
        deflections += 1

    if deflections >= 3:
        move = "C"

    return move

def almanac(lastMove="C", deflections=0):
    global deflections_almanac
    move = "D"  # C = cooperate, D = deflect

    if lastMove == 'D':
        deflections_almanac += 1
        move = 'D'
        deflections += 1
        if deflections_almanac == 2:
            deflections_almanac = 0
            move = 'C'  # Apologising

        elif deflections_almanac > 2:
            move = "C"

    if lastMove == "D":
        move = "D"
        deflections += 1

    return move

def lana(lastMove="C", deflections=0):
    global cCount
    global deflectX2
    move = "C"
    deflectX2 = False
    
    if lastMove == "D":
        move = "C"
        deflectX2 = True

    if deflectX2:
        move = random.randint(0, 10)
        if move < 7:
            move = "C"
        else:
            move = "D"
            deflections += 1
        deflectX2 = False

    if lastMove == "C":
        cCount += 1 
        if cCount >= 2:
            cCount = 0
            move = "D"
            deflections += 1

    return move


p1_points = 0
p2_points = 0
p3_points = 0
p4_points = 0
p5_points = 0
p6_points= 0

# Lists to store points for plotting
ben_points = []
ben2_points = []
almanac_points = []
lana_points = []
ray_points = []
forlot_points = []

for i in range(20):
    last_ben_move = almanac(ben())
    last_ben2_move = almanac(ben2)
    last_almanac_move = ben(almanac())
    last_lana_move = almanac(lana())
    last_ray_move = almanac(ray())
    last_forlot_move = almanac(forlot())

    # Calculate points for each iteration
    p1_points, p2_points, p3_points, p4_points, p5_points, p6_points = pointCalc(last_ben_move, last_almanac_move, last_lana_move, last_ray_move, last_forlot_move, last_ben2_move, p1_points, p2_points, p3_points, p4_points, p5_points, p6_points, 'ben', 'ben2', 'almanac', 'lana', 'ray', 'forlot')

    # Append points to lists
    ben_points.append(p1_points)
    ben2_points.append(p6_points)
    almanac_points.append(p2_points)
    lana_points.append(p3_points)
    ray_points.append(p4_points)
    forlot_points.append(p5_points)

    print("ben:", last_ben_move)
    print("ben2:", last_ben2_move)
    print("almanac:", last_almanac_move)
    print("lana:", last_lana_move)
    print("ray:", last_ray_move)
    print("forlot:", last_forlot_move)

# Plotting
plt.plot(ben_points, color='blue', label='Ben')
plt.plot(ben2_points, color='pink', label='Ben2')
plt.plot(almanac_points, color='brown', label='Almanac')
plt.plot(lana_points, color='green', label='Lana')
plt.plot(ray_points, color='orange', label='Ray')
plt.plot(forlot_points, color='purple', label='Forlot')
plt.xlabel('Iterations')
plt.ylabel('Points')
plt.title('Points Accumulation Over Iterations (With two incrediably forgiving)')
plt.legend()
plt.show()