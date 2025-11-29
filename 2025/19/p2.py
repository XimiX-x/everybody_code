import re
import numpy as np
import pygame

### Works also for part 3 since it's the same problem and part 1 since it's juste a subproblem of it

wlls = [[]]

with open("p2.txt") as file :
    for lines in file :
        line = [int(num) for num in re.findall("\d+", lines)] # type: ignore
        if len(wlls[0]) == 0 :
            wlls[0].append(line)
        else :
            if wlls[-1][0][0] == line[0] :
                wlls[-1].append(line)
            else :
                wlls.append([line])

walls = [[[w for w in wa] for wa in wal] for wal in wlls]
for wall in walls[0] :
    wall[2] = min(wall[0] - wall[1]+1, wall[2])
i = 0
while i < len(walls[0]) :
    if walls[0][i][2] < 0 :
        np.delete(walls[0], i)
    else :
        i += 1

for i in range(1, len(walls)) :
    delta_x = walls[i][0][0] - walls[i-1][0][0]
    for wall in walls[i] :
        wall_i = np.inf
        for prev in walls[i-1] :
            wall_i = min(wall_i, max(wall[1], prev[1]-delta_x))
            if wall_i == wall[1] :
                break
        if wall_i%2 != walls[i][0][0]%2 :
            wall_i += 1
        wall_p = -np.inf
        for prev in walls[i-1] :
            wall_p = max(wall_p, min(wall[1]+wall[2], prev[1] + prev[2] + delta_x))
            if wall_p == wall[2] :
                break
        wall[2] = wall_p- wall_i
        wall[1] = wall_i

for end in walls[-1] :
    if end[2] >= 1 :
        end[1] -= 2
        while True :
            end[1] += 2
            walls_prot = [[[w for w in wa] for wa in wal] for wal in walls]
            walls_prot[-1] = [end]
            for i in range(len(walls)-2, -1, -1) :
                delta_x = walls_prot[i+1][0][0] - walls_prot[i][0][0]
                for cour in walls_prot[i] :
                    cour1 = np.inf
                    for pred in walls_prot[i+1] :
                        cour1 = min(cour1, max(cour[1], pred[1]-delta_x))
                        if cour1 == cour[1] :
                            break
                    if cour1%2 != cour[0]%2 :
                        cour1 += 1
                    cour[1] = cour1
                for j, cour in enumerate(walls[i]) :
                    if cour[1] < walls[i][j][1] + walls[i][j][2] :
                        break
                else :
                    break
            else :
                walls = walls_prot
                break
        break

def feasible() :
    x, y = 0, 0
    i = 0
    for wall in walls :
        delta_x = wall[0][0]-x
        for fut in wall :
            delta_y = fut[1] - y
            if abs(delta_y) <= delta_x and delta_y % 2 == delta_x % 2 :
                break
        else :
            return False, i
        x, y = fut[0], fut[1]
        i += 1
    for end in walls[-1] :
        if end[2] >= 1 :
            return end[1] + (end[0]-end[1])/2

print("\n", feasible())

### We make a cool plot

def compute_traj() :
    pos = [0 for _ in range(walls[-1][0][0]+1)]
    x, y = 0, 0
    for wall in walls :
        delta_x = wall[0][0] - x
        for fut in wall :
            delta_y = fut[1] - y
            if abs(delta_y) <= delta_x and delta_y % 2 == delta_x % 2 :
                dep = np.sign(delta_y)
                if dep == 0 :
                    dep = 1
                for i in range(1, abs(delta_y)+1) :
                    y = y+dep
                    pos[x+i] = y
                dep = 1
                for i in range(abs(delta_y)+1, delta_x+1) :
                    y = y+dep
                    pos[x+i] = y
                    dep = -dep
                x = x + delta_x
                break
    return pos

pos = compute_traj()
len_x, len_y = len(pos), max(pos)+1
size_y = 10
size_x = 10
offset_x = 1900/2
offset_y = 500

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

j = 0
focus = pos[j]
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False
    screen.fill((0,0,0))
    if abs(focus-pos[j]) > 1 :
        focus = pos[j-2]
    for wllss in wlls :
        pygame.draw.rect(screen, (255, 255, 255), (offset_x + (wllss[0][0] - j)*size_x, 0, size_x, 1000))
        for wall in wllss :
            pygame.draw.rect(screen, (0, 0, 0), (offset_x + (wall[0]-j)*size_x,1000 - offset_y - (wall[1]+wall[2]-focus)*size_y, size_x, wall[2]*size_y))
    for x in range(j):
        y= pos[x]
        pygame.draw.rect(screen, (255, 0, 255), (offset_x + (x-j)*size_x, 1000 - offset_y - (y+1-focus)*size_y, size_x, size_y))
    pygame.draw.line(screen, (255, 255, 255), (0, 1000-offset_y + focus*size_y), (2000, 1000-offset_y + focus*size_y))
    j = (j+1)%len(pos)
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(60)

pygame.quit()