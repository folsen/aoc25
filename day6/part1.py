from functools import reduce
from operator import mul

lines = []
with open("input.txt") as file:
    lines = [line.rstrip().split() for line in file]


def apply_op(char, nums):
    ints = list(map(int, nums))
    if char == "*":
        return reduce(mul, list(map(int, ints)), 1)
    elif char == "+":
        return sum(ints)
    return 0


p1 = 0
for i in range(len(lines[0])):
    p1 += apply_op(lines[4][i], [lines[0][i], lines[1][i], lines[2][i], lines[3][i]])
print("P1:", p1)
