# Pretty-print a dict matrix
def pp(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end="")
        print("")


lines = []
# Making everything into dict because then i can get(X,".") and return default empty if i'm out of bounds
with open("input.txt") as file:
    lines = [dict(enumerate(line.rstrip())) for line in file]

input = dict(enumerate(lines))
rows = len(input)
cols = len(input.get(0, {}))


def accessible_rolls(input, remove=False):
    p1 = 0
    for i in range(rows):
        for j in range(cols):
            filled = 0
            for x, y in [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]:
                if input.get(x, {}).get(y, ".") == "@":
                    filled += 1
            if filled < 4 and input[i][j] == "@":
                if remove:
                    input[i][j] = "."
                p1 += 1
    return p1


print("P1:", accessible_rolls(input))

state = input
removed = 0
while accessible_rolls(state) > 0:
    removed += accessible_rolls(state, True)

print("P2:", removed)
