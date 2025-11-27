import numpy as np

# mapp = []
# vx = vy = 0

# with open("p1.txt") as file :
#     i = 0
#     for lines in file :
#         if '@' in lines :
#             vx, vy = lines.index('@'), i
#             line = lines.split('@')
#             mapp.append([int(c) for c in line[0]] + [0] + [int(c) for c in line[1].split('\n')[0]])
#         else :
#             mapp.append([int(c) for c in lines.split('\n')[0]])
#         i += 1


# for i in range(len(mapp)) :
#     for j in range(len(mapp[0])) :
#         if (i-vx)**2 + (j-vy)**2 > 100 :
#             mapp[i][j] = 0

# print(np.sum(mapp))

# In one line hehe :
print(np.sum([[0 if i**2 + j**2>100 else car for j, car in enumerate(elem, start = -(np.argmin([[int(c) for c in line.split()[0]] if not '@' in line else [int(c) for c in line.split("@")[0]] + [0] + [int(c) for c in line.split("@")[1].split()[0]] for line in open("p1.txt")])//len([[int(c) for c in line.split()[0]] if not '@' in line else [int(c) for c in line.split("@")[0]] + [0] + [int(c) for c in line.split("@")[1].split()[0]] for line in open("p1.txt")][1])))] for i, elem in enumerate([[int(c) for c in line.split()[0]] if not '@' in line else [int(c) for c in line.split("@")[0]] + [0] + [int(c) for c in line.split("@")[1].split()[0]] for line in open("p1.txt")], start = -(np.argmin([[int(c) for c in line.split()[0]] if not '@' in line else [int(c) for c in line.split("@")[0]] + [0] + [int(c) for c in line.split("@")[1].split()[0]] for line in open("p1.txt")])//len([[int(c) for c in line.split()[0]] if not '@' in line else [int(c) for c in line.split("@")[0]] + [0] + [int(c) for c in line.split("@")[1].split()[0]] for line in open("p1.txt")][0])))]))