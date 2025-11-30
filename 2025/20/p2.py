import pygame
import heapq

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

width, heigth = 10, 11
offset_x, offset_y = 950, 0
middle_x = 0
def draw_line(line, j) :
    for i, c in enumerate(line) :
        if c != '.' :
            if not (i+j)%2 :
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*j))
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i-middle_x)*width/2,offset_y + heigth*j), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*(j+1)))
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*j))

trampo = ('T', 'E', 'S')
S, E = None, None
graph = set()

with open("p2.txt") as file :
    input = ["", ""]
    input[0] = file.readline().split()[0]
    middle_x = len(input[0])//2
    draw_line(input[0], 0)
    j = 0
    for line in file :
        input[1] = line.split()[0]
        draw_line(input[1], j+1)
        for i, c in enumerate(input[0]) :
            if c in trampo :
                if c == 'E' :
                    E = (i, j)
                    if (i+j)%2 :
                        pygame.draw.polygon(screen, (255, 0, 255), ((offset_x + (i-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*j)))
                    else :
                        pygame.draw.polygon(screen, (255, 0, 255), ((offset_x + (i-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*(j+1))))
                if c == 'S' :
                    S = (i, j)
                    if (i+j)%2 :
                        pygame.draw.polygon(screen, (0, 255, 255), ((offset_x + (i-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*j)))
                    else :
                        pygame.draw.polygon(screen, (0, 255, 255), ((offset_x + (i-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*(j+1))))
                if i < len(input[0])-1 and input[0][i+1] in trampo :
                    graph.add((i, j))
                    graph.add((i+1, j))
                    if (i+j)%2 :
                        pygame.draw.line(screen, (0, 255, 0), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*j))
                    else :
                        pygame.draw.line(screen, (0, 255, 0), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*j))
                if (j+i)%2 and input[1][i] in trampo:
                    graph.add((i, j))
                    graph.add((i, j+1))
                    pygame.draw.line(screen, (0, 255, 0), (offset_x + (i-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*(j+1)))
        clock = pygame.time.Clock()
        clock.tick(20)
        pygame.display.update()
        input[0] = input[1]
        j += 1

for i, c in enumerate(input[0]) :
    if c == 'S' :
        S = (i, j)
        if (i+j)%2 :
            pygame.draw.polygon(screen, (0, 255, 255), ((offset_x + (i-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*j)))
        else :
            pygame.draw.polygon(screen, (0, 255, 255), ((offset_x + (i-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+2-middle_x)*width/2, offset_y + heigth*j), (offset_x + (i+1-middle_x)*width/2, offset_y + heigth*(j+1))))

q = []
heapq.heappush(q, (0, S))
pred = {S : (0, S)}

while len(q) :
    dist, cour = heapq.heappop(q)
    if cour == E :
        break
    i, j = cour
    if (i+1, j) in graph :
        if not (i+1, j) in pred :
            pred[(i+1, j)] = (dist+1, (i, j))
            heapq.heappush(q, (dist+1, (i+1, j)))
    if (i-1, j) in graph :
        if not (i-1, j) in pred :
            pred[(i-1, j)] = (dist+1, (i, j))
            heapq.heappush(q, (dist+1, (i-1, j)))
    if (i+j)%2 and (i, j+1) in graph :
        if not (i, j+1) in pred :
            pred[(i, j+1)] = (dist+1, (i, j))
            heapq.heappush(q, (dist+1, (i, j+1)))
    if (not (i+j)%2) and (i, j-1) in graph :
        if not (i, j-1) in pred :
            pred[(i, j-1)] = (dist+1, (i, j))
            heapq.heappush(q, (dist+1, (i, j-1)))

print(dist) # type: ignore

path = [E]

while path[-1] != S :
    path.append(pred[path[-1]][1])

path.reverse()

run = True

j = 0
while j < len(path)+1 :
    for i in range(1, j) :
        i1, j1 = path[i-1] # type: ignore
        i2, j2 = path[i] # type: ignore
        if i2 > i1 :
            if (i1+j1)%2 :
                pygame.draw.line(screen, (255, 0, 0), (offset_x + (i1+2-middle_x)*width/2, offset_y + heigth*(j1+1)), (offset_x + (i1+1-middle_x)*width/2, offset_y + heigth*j1))
            else :
                pygame.draw.line(screen, (255, 0, 0), (offset_x + (i1+1-middle_x)*width/2, offset_y + heigth*(j1+1)), (offset_x + (i1+2-middle_x)*width/2, offset_y + heigth*j1))
        elif j2 > j1 :
            pygame.draw.line(screen, (255, 0, 0), (offset_x + (i1-middle_x)*width/2, offset_y + heigth*(j1+1)), (offset_x + (i1+2-middle_x)*width/2, offset_y + heigth*(j1+1)))
        elif j1 > j2 :
            pygame.draw.line(screen, (255, 0, 0), (offset_x + (i2-middle_x)*width/2, offset_y + heigth*(j2+1)), (offset_x + (i2+2-middle_x)*width/2, offset_y + heigth*(j2+1)))
        else :
            if (i2+j2)%2 :
                pygame.draw.line(screen, (255, 0, 0), (offset_x + (i2+2-middle_x)*width/2, offset_y + heigth*(j2+1)), (offset_x + (i2+1-middle_x)*width/2, offset_y + heigth*j2))
            else :
                pygame.draw.line(screen, (255, 0, 0), (offset_x + (i2+1-middle_x)*width/2, offset_y + heigth*(j2+1)), (offset_x + (i2+2-middle_x)*width/2, offset_y + heigth*j2))
    j = j+1
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False

pygame.quit()