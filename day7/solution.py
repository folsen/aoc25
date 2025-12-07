input = []
with open("input.txt") as file:
    input = [list(line.replace("\n", "")) for line in file]

rows = len(input)
cols = len(input[0])

p1 = 0
for i in range(rows - 1):
    for j in range(cols):
        if input[i][j] == "S" or input[i][j] == "|":
            if input[i + 1][j] == "^":
                input[i + 1][j - 1] = "|"
                input[i + 1][j + 1] = "|"
                p1 += 1
            else:
                input[i + 1][j] = "|"

print("P1:", p1)

start = 0
cache = dict()
for i in range(cols):
    if input[0][i] == "S":
        start = i
        break


def step(i, j):
    if cache.get((i, j)) is not None:
        return cache[(i, j)]
    if i == rows - 1:
        return 1
    if input[i + 1][j] == "^":
        lc = step(i + 1, j - 1)
        rc = step(i + 1, j + 1)
        cache[(i, j)] = lc + rc
        return lc + rc
    else:
        c = step(i + 1, j)
        cache[(i, j)] = c
        return c


print("P2:", step(0, start))
