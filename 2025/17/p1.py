import numpy as np

mapp = []
vx = vy = 0

with open("p1.txt") as file :
    i = 0
    for lines in file :
        if '@' in lines :
            vx, vy = lines.index('@'), i
            line = lines.split('@')
            mapp.append([int(c) for c in line[0]] + [0] + [int(c) for c in line[1].split('\n')[0]])
        else :
            mapp.append([int(c) for c in lines.split('\n')[0]])
        i += 1


for i in range(len(mapp)) :
    for j in range(len(mapp[0])) :
        if (i-vx)**2 + (j-vy)**2 > 100 :
            mapp[i][j] = 0

print(np.sum(mapp))