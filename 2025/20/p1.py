import pygame

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 25)

width, heigth = 70, 78
offset_x, offset_y = 550, 0
def draw_line(line, j) :
    for i, c in enumerate(line) :
        if c != '.' :
            if not (i+j)%2 :
                pygame.draw.line(screen, (255, 255, 255), (offset_x + i*width/2, offset_y + heigth*j), (offset_x + (i+2)*width/2, offset_y + heigth*j))
                pygame.draw.line(screen, (255, 255, 255), (offset_x + i*width/2,offset_y + heigth*j), (offset_x + (i+1)*width/2, offset_y + heigth*(j+1)))
                pygame.draw.line(screen, (255, 255, 255), (offset_x + (i+1)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2)*width/2, offset_y + heigth*j))
                text_surface = my_font.render(c, False, (255, 255, 255))
                screen.blit(text_surface, (offset_x - 7 + (i+1)*width/2,offset_y - 15 + heigth*(j+1/2)))
            else :
                text_surface = my_font.render(c, False, (255, 255, 255))
                screen.blit(text_surface, (offset_x - 5 + (i+1)*width/2,offset_y + 3 + heigth*(j+1/2)))

with open("p1.txt") as file :
    input = ["", ""]
    input[0] = file.readline().split()[0]
    draw_line(input[0], 0)
    res = 0
    j = 0
    for line in file :
        input[1] = line.split()[0]
        draw_line(input[1], j+1)
        for i, c in enumerate(input[0]) :
            if c == 'T' :
                if i < len(input[0])-1 and input[0][i+1] == 'T' :
                    res += 1
                    if (i+j)%2 :
                        pygame.draw.line(screen, (0, 255, 0), (offset_x + (i+2)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+1)*width/2, offset_y + heigth*j))
                    else :
                        pygame.draw.line(screen, (0, 255, 0), (offset_x + (i+1)*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2)*width/2, offset_y + heigth*j))
                if (j+i)%2 and input[1][i] == 'T':
                    res += 1
                    pygame.draw.line(screen, (0, 255, 0), (offset_x + i*width/2, offset_y + heigth*(j+1)), (offset_x + (i+2)*width/2, offset_y + heigth*(j+1)))
        clock = pygame.time.Clock()
        clock.tick(10)
        pygame.display.update()
        input[0] = input[1]
        j += 1

print(res)

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False

pygame.quit()