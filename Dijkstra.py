INF = 10000000
s = []
q = [0, 1, 2, 3, 4, 5]
d = [0, INF, INF, INF, INF, INF]
vertex = [
    (0, 1, 10),
    (0, 2, 30),
    (0, 3, 15),
    (1, 4, 20),
    (2, 5, 5),
    (3, 2, 5),
    (3, 5, 20),
    (4, 5, 20),
    (5, 3, 20)
]

while len(q) > 0:
    minNode = sorted([(x, d[x]) for x in q], key=lambda x: x[1])[0][0]
    q.remove(minNode)
    s.append(minNode)
    edges = [x for x in vertex if x[0] == minNode]
    for start, end, value in edges:
        if d[end] > d[start] + value:
            d[end] = d[start] + value
    print(d)