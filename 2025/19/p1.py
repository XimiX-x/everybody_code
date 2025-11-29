import re
import numpy as np
import pygame

wlls = []

with open("test.txt") as file :
    for lines in file :
        line = [int(num) for num in re.findall("\d+", lines)] # type: ignore
        wlls.append(line)

walls = np.array([[w for w in wa] for wa in wlls])
walls[0] = [walls[0][0], walls[0][1], min(walls[0][0]-walls[0][1]+1, walls[0][2])]
for i in range(1, len(walls)) :
    delta_x = walls[i][0] - walls[i-1][0]
    walls_i = max(walls[i][1], walls[i-1][1]-delta_x)
    if walls_i%2 != walls[i][0]%2 :
        walls_i += 1
    walls[i][2] = min(walls[i][1]+walls[i][2], walls[i-1][1] + walls[i-1][2] + delta_x) - walls_i
    walls[i][1] = walls_i

walls[-1, 1] -= 2
while True :
    walls[-1, 1] += 2
    walls_prot = np.array([[w for w in wal] for wal in walls])
    for i in range(len(walls)-2, -1, -1) :
        delta_x = walls_prot[i+1, 0]- walls_prot[i, 0]
        walls_prot[i, 1] = max(walls[i, 1], walls_prot[i+1, 1]-delta_x)
        if (walls_prot[i, 1] - walls_prot[i+1, 1]) % 2 != delta_x % 2 :
            walls_prot[i, 1] += 1
        if walls_prot[i, 1] > walls[i, 1] + walls[i, 2] :
            break
    else :
        walls = walls_prot
        break

def feasible() :
    x, y = 0, 0
    i = 0
    for wall in walls :
        delta_x, delta_y = wall[0]-x, wall[1] - y
        if abs(delta_y) > delta_x :
            return False, i
        if delta_y % 2 != delta_x % 2 :
            return False, i
        x, y = wall[0], wall[1]
        i += 1
    return walls[-1][1] + (walls[-1][0]-walls[-1][1])/2

print("\n", feasible())

### We make a cool plot

def compute_traj() :
    pos = [0 for _ in range(walls[-1][0]+1)]
    x, y = 0, 0
    for wall in walls :
        delta_x, delta_y = wall[0]-x, wall[1] - y
        dep = np.sign(delta_y)
        for i in range(1, abs(delta_y)+1) :
            y = y+dep
            pos[x+i] = y
        for i in range(abs(delta_y)+1, delta_x+1) :
            y = y+dep
            pos[x+i] = y
            dep = -dep
        x = x + delta_x
    return pos

pos = compute_traj()
len_x, len_y = len(pos), max(pos)+1
size = min(1850/len_x, 950/len_y)
offset_x = (1900-size*len_x)/2
offset_y = 1000 - (1000-size*len_y)/2

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

j = 0
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False
    screen.fill((0,0,0))
    for wall in wlls :
        pygame.draw.rect(screen, (255, 255, 255), (offset_x + wall[0]*size, offset_y - wall[1]*size, size, wall[1]*size))
        pygame.draw.rect(screen, (255, 255, 255), (offset_x + wall[0]*size, 1000-offset_y, size, (len_y - wall[2] - wall[1])*size))
    for x in range(j):
        y= pos[x]
        pygame.draw.rect(screen, (255, 0, 255), (offset_x + x*size, offset_y - (y+1)*size, size, size))
    j = (j+1)%len(pos)
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(20)

pygame.quit()
