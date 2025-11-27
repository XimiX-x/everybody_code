graph = []
entries = []

with open("p2.txt") as file :
    for lines in file :
        line = lines.split()
        if line :
            match line[0] :
                case "Plant" :
                    graph.append([int(line[4][:-1])])
                case "-" :
                    if line[1] == "branch" :
                        graph[-1].append((int(line[4]), int(line[7])))
                case default :
                    entries.append([int(num) for num in line])

res = 0
for entry in entries :
    emit = [0 for _ in graph]
    j = 0
    for i, elem in enumerate(graph) :
        if len(elem) == 1 :
            if elem[0] <= entry[j] :
                emit[i] = 1
            j += 1
        else :
            em = 0
            for pred, thick in elem[1:] :
                em += emit[pred-1]*thick
            if em >= elem[0] :
                emit[i] = em
    res += emit[-1]

print(res)