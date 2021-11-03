"""
Breadth-First Search (BFS)
"""
def BFS(s):
    global color, res
    color[s] = "GRAY"
    queue = [s]
    while queue:
        u = queue.pop(0)
        res.append(u)
        for v in adjlist[u]:
            if color[v] == "WHITE":
                color[v] = "GRAY"
                queue.append(v)
        color[u] = 'BLACK'

color = {u: "WHITE" for u in adjlist}
res = []

for u in adjlist:
    if color[u] == "WHITE":
        BFS(u)

print(res) #[0, 1, 5, 6, 2, 7, 4, 11, 8, 10, 3, 9]

"""
This is to generate Adj List Representation for Graph
"""
n = 12
m = 18
adjlist = {i:[] for i in range(n)}
for i in range(6):
    adjlist[i].extend(((i+1)%6, (i+5)%6))
    adjlist[i].append(i+6)
for i in range(6, 12):
    adjlist[i].append(i-6)
    adjlist[i].extend((6+(i+2)%6, 6+(i+4)%6))

"""
{0: [1, 5, 6],
 1: [2, 0, 7],
 2: [3, 1, 8],
 3: [4, 2, 9],
 4: [5, 3, 10],
 5: [0, 4, 11],
 6: [0, 8, 10],
 7: [1, 9, 11],
 8: [2, 10, 6],
 9: [3, 11, 7],
 10: [4, 6, 8],
 11: [5, 7, 9]}
"""
