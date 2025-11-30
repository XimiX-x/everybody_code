import pygame
import heapq

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

input = []
with open("p3.txt") as file :
    for lines in file :
        input.append(lines.split()[0])
y_bot = len(input)-1

bot = input[-1]
if 'T' in bot :
    x_bot = bot.index('T')
elif 'S' in bot :
    x_bot = bot.index('S')
else :
    x_bot = bot.index('E')

trampo = ('T', 'E', 'S')
graph = {}

def rot(i, j) :
    return x_bot + j - (i-j)//2, y_bot - (i-j+1)//2 - j

for j, line in enumerate(input) :
    for i, c in enumerate(line) :
        if c in trampo :
            if c == 'E' :
                E1 = (j, i)
                i1, j1 = rot(i, j)
                E2 = (j1, i1)
                i2, j2 = rot(i1, j1)
                E3 = (j2, i2)
            elif c == 'S' :
                S = (i, j)
        if c != '.' :
            x, y = i, j
            for rota in (0, 1, 2) :
                succ = []
                j2, i2 = rot(x, y)
                if input[y][x] in trampo :
                    if input[i2][j2] in trampo :
                        succ.append(((i2, j2), (rota+1)%3))
                    if x > 0 and input[y][x-1] != '.' :
                        j3, i3 = rot(x-1, y)
                        if input[i3][j3] in trampo :
                            succ.append(((i3, j3), (rota+1)%3))
                    if x < len(input[0])-1 and input[y][x+1] != '.' :
                        j3, i3 = rot(x+1, y)
                        if input[i3][j3] in trampo :
                            succ.append(((i3, j3), (rota+1)%3))
                    if not (x+y)%2 :
                        if y != 0 :
                            j3, i3 = rot(x, y-1)
                            if input[i3][j3] in trampo :
                                succ.append(((i3, j3), (rota+1)%3))
                    else :
                        j3, i3 = rot(x, y+1)
                        if input[i3][j3] in trampo :
                            succ.append(((i3, j3), (rota+1)%3))
                graph[((y, x), rota)] = succ
                x, y = j2, i2

h = [(0, (S, 0))] # type: ignore
pred = {(S, 0) : ((S, 0))} # type: ignore
while len(h) :
    dist, node = heapq.heappop(h)
    coord, rota = node
    match rota :
        case 0 :
            if coord == E1 : # type: ignore
                break
        case 1 :
            if coord == E2 : # type: ignore
                break
        case 2 :
            if coord == E3 : # type: ignore
                break
    for succ in graph[node] :
        if not succ in pred.keys() :
            pred[succ] = node
            heapq.heappush(h, (dist+1, succ))

print(dist) # type: ignore


width, heigth = 11, 12
offset_x, offset_y = 950, (1000-(y_bot*heigth))/2
def draw_line(line, j) :
    for i, c in enumerate(line) :
        if c != '.' :
            if not (i+j)%2 :
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j))
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i-x_bot)*width/2,offset_y + heigth*j), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1)))
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j))

def affiche_map(tick = 0, display = False):
    j = 0
    for line in input :
        draw_line(line, j)
        for i, c in enumerate(line) :
            if c in trampo :
                if c == 'E' :
                    if (i+j)%2 :
                        pygame.draw.polygon(screen, (255, 0, 255), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*j)))
                    else :
                        pygame.draw.polygon(screen, (255, 0, 255), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1))))
                if c == 'S' :
                    if (i+j)%2 :
                        pygame.draw.polygon(screen, (0, 255, 255), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*j)))
                    else :
                        pygame.draw.polygon(screen, (0, 255, 255), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1))))
                if i < len(input[0])-1 and input[0][i+1] in trampo :
                    if (i+j)%2 :
                        pygame.draw.line(screen, (0, 255, 0), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*j))
                    else :
                        pygame.draw.line(screen, (0, 255, 0), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j))
                if (j+i)%2 and input[1][i] in trampo:
                    pygame.draw.line(screen, (0, 255, 0), (offset_x + (i-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*(j+1)))
        clock = pygame.time.Clock()
        clock.tick(tick)
        if display :
            pygame.display.update()
        j += 1

affiche_map(20, True)

path = [node] # type: ignore
while path[-1] != (S, 0) : # type: ignore
    path.append(pred[path[-1]])

run = True

k = len(path)-1
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False
    screen.fill((0, 0, 0))
    affiche_map()
    for index in range(len(path)-1, k-1, -1) :
        pos, rota = path[index]
        j, i = pos
        for _ in range((3-rota)%3) :
            i, j = rot(i, j)
        if (i+j)%2 :
            pygame.draw.polygon(screen, (0, 255, 0), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*j)))
        else :
            pygame.draw.polygon(screen, (0, 255, 0), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1))))
    pos, rota = path[index] # type: ignore
    j, i = pos
    if (i+j)%2 :
        pygame.draw.polygon(screen, (255, 0, 0), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*j)))
    else :
        pygame.draw.polygon(screen, (255, 0, 0), ((offset_x + (i-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+2-x_bot)*width/2, offset_y + heigth*j), (offset_x + (i+1-x_bot)*width/2, offset_y + heigth*(j+1))))
    clock = pygame.time.Clock()
    clock.tick(10)
    pygame.display.update()
    k = (k-1)%len(path)

pygame.quit()