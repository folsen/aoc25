from functools import reduce
from operator import mul

lines = []
with open("input.txt") as file:
    lines = [line.replace("\n", "") for line in file]


def apply_op(char, nums):
    ints = list(map(int, nums))
    if char == "*":
        return reduce(mul, list(map(int, ints)), 1)
    elif char == "+":
        return sum(ints)
    return 0


# Flip everything so it's parseable left-right
flipped = ""
for i in range(len(lines[0]) - 1, -1, -1):
    for j in range(len(lines)):
        flipped += lines[j][i]
flipped = flipped.replace("+", " +").replace("*", " *").split()

p2 = 0
stash = []
for e in flipped:
    if e == "+" or e == "*":
        p2 += apply_op(e, stash)
        stash = []
    else:
        stash.append(e)
print("P2:", p2)
