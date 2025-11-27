graph = []

with open("p1.txt") as file :
    for lines in file :
        line = lines.split()
        if len(line) :
            match line[0] :
                case "Plant" :
                    graph.append([int(line[4][:-1])])
                case "-" :
                    if line[1] == "branch" :
                        graph[-1].append((int(line[4]), int(line[7])))

emit = [0 for _ in graph]
for i, elem in enumerate(graph) :
    if len(elem) == 1 :
        if elem[0] <= 1 :
            emit[i] = 1
    else :
        em = 0
        for pred, thick in elem[1:] :
            em += emit[pred-1]*thick
        if em >= elem[0] :
            emit[i] = em

print(emit[-1])