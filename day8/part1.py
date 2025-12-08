from numpy import array
from numpy.linalg import norm

N = 1000
input = []
with open("input.txt") as file:
    input = [array(list(map(int, line.rstrip().split(",")))) for line in file]
boxes = len(input)
shortest_connections = []

for i in range(boxes):
    for j in range(i + 1, boxes):
        dist = norm(input[i] - input[j])
        shortest_connections.append((input[i], input[j], dist))

shortest_connections.sort(key=lambda x: x[2])
connected_sets = []
for i in range(N):
    a, b, _ = shortest_connections[i]
    a = str(a)
    b = str(b)
    a_set = None
    b_set = None
    for cs in connected_sets:
        if a in cs and b in cs:
            a_set = cs
            b_set = cs
        if a in cs:
            a_set = cs
        elif b in cs:
            b_set = cs
    if a_set is not None and b_set is None:
        a_set.add(b)
    elif a_set is None and b_set is not None:
        b_set.add(a)
    elif a_set is not None and b_set is not None:
        i = 0
        while i < len(connected_sets):
            if connected_sets[i] == a_set or connected_sets[i] == b_set:
                connected_sets = connected_sets[:i] + connected_sets[i + 1 :]
                i -= 1
            i += 1
        connected_sets.append(a_set.union(b_set))
    else:
        connected_sets.append(set([a, b]))

connected_sets.sort(key=lambda s: len(s), reverse=True)
p1 = 1
for i in range(3):
    p1 *= len(connected_sets[i])

print("P1:", p1)
