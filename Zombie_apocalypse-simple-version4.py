import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 100
p = 0.65  ##population density
p11 = 0.5 ##probability of transforming into zombie lv1
p12 = 0.3 ##probability of transforming into zombie lv2
p13 = 0.05 ##probability of transforming into zombie lv3
p2 = 0.01 ##probability of recovery rate of zombie lv1 & lv2
p3 = 0.03
awareness = 3000
r = 1

def initialize():
    global status, status2, num
    status = zeros([L, L])
    for x in range(L):
        for y in range(L):
            status[x, y] = 1 if random() < p else 0
    status[int(L/2), int(L/2)] = 5 ##Initial zombie
    status2 = zeros([L, L])
    num = 0
    
def observe():
    global status
    cla() # to clear the visualization space
    imshow(status, vmin = 0, vmax = 5)



##Condition Setting
##Antidote won't be appeared after a period of time
##When civilian is bitten by zombies, he/she has chance transforming into different levels of zombies
##After injecting antidote, zombie has chances recoverying to normal civilian and won't be affected agiain
##Normal people who is injected antidote also won't be affected

      
def update():
    global status, status2, num, antidote
    for x in range(L):
        for y in range(L):
            # if you are 0, 2 or 5, stay unchanged
            if status[x,y] in[3,4,5]:
                num += 1
            if status[x,y] in [0,2,5]:
                status2[x,y] = status[x,y]
            elif status[x,y] in [3,4]:
                n1 = 0
                if num >= awareness:
                    for dx in range(-r, r+1):
                        for dy in range(-r, r+1):
                            if 0 <= x+dx < L and 0 <= y+dy < L:
                                n1 += 1 if status[x+dx, y+dy] == 2 else 0
                            if n1>= 1:
                                status2[x,y] = 2 if random() <= p2 else status[x,y]
                            else:
                                status2[x,y] = status[x,y]
                else:
                    status2[x,y] = status[x,y]
                    
            else:
                if num >= awareness:
                    n2 = 0
                    if random() <= p3:
                        status2[x,y] = 2
                    else:
                        for dx in range(-r, r+1):
                            for dy in range(-r, r+1):                      
                                if 0 <= x+dx < L and 0 <= y+dy < L:
                                    n2 += 1 if status[x+dx, y+dy] in [3,4,5] else 0
                                status2[x, y] = np.random.choice([3,4,5], p=[p11/0.85,p12/0.85,p13/0.85]) if n2 > 0 else 1
                  
                else:
                    n3 = 0
                    for dx in range(-r, r+1):
                        for dy in range(-r, r+1):
                            if 0 <= x+dx < L and 0 <= y+dy < L:
                                #Normal civilian(1): will transform into civilian(1), civilian w/ anitdote(2), Zombie lv1(3),
                                #Zombie lv2(4), Zombie lv3(5)
                                n3 += np.random.choice([1,3,4,5], p=[1-p11-p12-p13,p11,p12,p13]) if status[x+dx, y+dy] >= 2 else 0
                            if n3 == 1:
                                status2[x, y] = 1
                            elif n3 >= 2:
                                status2[x, y] = np.random.choice([3,4,5], p=[p11/0.85,p12/0.85,p13/0.85])
                            else:
                                status2[x, y] = status[x, y]
                                ##Besides spreading, the infection process should be still on-going simultaneously

                
    status, status2 = status2, status

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
