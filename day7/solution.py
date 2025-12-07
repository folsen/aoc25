from functools import cache

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
for i in range(cols):
    if input[0][i] == "S":
        start = i
        break


@cache
def step(i, j):
    if i == rows - 1:
        return 1
    if input[i + 1][j] == "^":
        return step(i + 1, j - 1) + step(i + 1, j + 1)
    else:
        return step(i + 1, j)


print("P2:", step(0, start))
