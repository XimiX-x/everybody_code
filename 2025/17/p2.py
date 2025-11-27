import numpy as np
from math import ceil

mapp = []
vx = vy = 0

with open("p2.txt") as file :
    i = 0
    for lines in file :
        if '@' in lines :
            vx, vy = lines.index('@'), i
            line = lines.split('@')
            mapp.append([int(c) for c in line[0]] + [0] + [int(c) for c in line[1].split('\n')[0]])
        else :
            mapp.append([int(c) for c in lines.split('\n')[0]])
        i += 1
mapp = np.array(mapp)

cost = np.array([0 for _ in range(ceil(np.sqrt(max(vx^2, (len(mapp)-vx)**2) + max(vy**2, (len(mapp[0]-vy)**2)))))])
for i in range(len(mapp)) :
    for j in range(len(mapp[0])) :
        dist = (i-vx)**2 + (j-vy)**2
        cost[ceil(np.sqrt(dist))-1] += mapp[i, j]

ind = np.argmax(cost)
print((ind+1)*cost[ind])