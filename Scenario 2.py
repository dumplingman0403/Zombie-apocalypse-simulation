import pycxsimulator
from pylab import *
import matplotlib
matplotlib.use('TkAgg')

L = 100  # Total field size (100 ---> 100x100)
p = 0.9  # population density
p11 = 0.05  # probability of transforming into zombie lv1
p12 = 0.3  # probability of transforming into zombie lv2
p13 = 0.5  # probability of transforming into zombie lv3
p21 = 0.01  # probability of recovery rate of zombie lv1
p22 = 0.005  # probability of recovery rate of zombie lv2
p3 = 0.15  # probability of dropping rate about the antidote
awareness = 3000  # Threshold of dropping the antidote
r = 1  # Infection range of neighborhood


def initialize():
    global status, status2, num
    status = zeros([L, L])
    for x in range(L):
        for y in range(L):
            status[x, y] = 1 if random() < p else 0
    status[int(L/2), int(L/2)] = 5  # Initial zombie
    status2 = zeros([L, L])
    num = 0  # The parameter for counting the numeber of zombies lv1, lv2, and lv3


def observe():
    global status
    cla()  # to clear the visualization space
    imshow(status, vmin=0, vmax=5)


# Condition Setting
# Antidote won't be appeared until reaching the threshold
# When the civilian is bitten by zombies, he/she has chance transforming into different levels of zombies
# After injecting antidote, zombie has chances recoverying to normal civilian and won't be affected agiain
# Normal people who is injected antidote also won't be affected


def update():
    global status, status2, num, antidote
    for x in range(L):
        for y in range(L):
            # Counting the number of all levels of zombies
            if status[x, y] in[3, 4, 5]:
                num += 1
            # if you are 0, 2 or 5, stay unchanged
            if status[x, y] in [0, 2, 5]:
                status2[x, y] = status[x, y]
            elif status[x, y] == 3:
                n1 = 0
                if num >= awareness:
                    for dx in range(-r, r+1):
                        for dy in range(-r, r+1):
                            if 0 <= x+dx < L and 0 <= y+dy < L:
                                n1 += 1 if status[x+dx, y+dy] == 2 else 0
                            if n1 >= 1:
                                status2[x, y] = 2 if random(
                                ) <= p21 else status[x, y]
                            else:
                                status2[x, y] = status[x, y]
                else:
                    status2[x, y] = status[x, y]
            elif status[x, y] == 4:
                n2 = 0
                if num >= awareness:
                    for dx in range(-r, r+1):
                        for dy in range(-r, r+1):
                            if 0 <= x+dx < L and 0 <= y+dy < L:
                                n2 += 1 if status[x+dx, y+dy] == 2 else 0
                            if n2 >= 1:
                                status2[x, y] = 2 if random(
                                ) <= p22 else status[x, y]
                            else:
                                status2[x, y] = status[x, y]
                else:
                    status2[x, y] = status[x, y]

            else:
                if num >= awareness:
                    if num <= awareness+20:
                        status2[x, y] = 2 if random() <= p3 else status[x, y]
                    else:
                        n3 = 0
                        if random() <= p3:
                            for dx in range(-r, r+1):
                                for dy in range(-r, r+1):
                                    if 0 <= x+dx < L and 0 <= y+dy < L:
                                        n3 += 1 if status[x +
                                                          dx, y+dy] == 2 else 0
                                    status2[x, y] = 2 if n3 > 0 else status[x, y]
                        else:
                            n4 = 0
                            for dx in range(-r, r+1):
                                for dy in range(-r, r+1):
                                    if 0 <= x+dx < L and 0 <= y+dy < L:
                                        n4 += 1 if status[x+dx,
                                                          y+dy] in [3, 4, 5] else 0
                                status2[x, y] = np.random.choice(
                                    [1, 3, 4, 5], p=[1-p11-p12-p13, p11, p12, p13]) if n4 > 0 else 1

                else:
                    n5 = 0
                    for dx in range(-r, r+1):
                        for dy in range(-r, r+1):
                            if 0 <= x+dx < L and 0 <= y+dy < L:
                                # Normal civilian(1): will transform into civilian(1), civilian w/ anitdote(2), Zombie lv1(3),
                                # Zombie lv2(4), Zombie lv3(5)
                                n5 += np.random.choice([1, 3, 4, 5], p=[
                                                       1-p11-p12-p13, p11, p12, p13]) if status[x+dx, y+dy] >= 3 else 0
                            if n5 == 1:
                                status2[x, y] = 1
                            elif n5 >= 2:
                                status2[x, y] = np.random.choice(
                                    [3, 4, 5], p=[p11/0.85, p12/0.85, p13/0.85])
                            else:
                                status2[x, y] = status[x, y]

    status, status2 = status2, status


pycxsimulator.GUI().start(func=[initialize, observe, update])
