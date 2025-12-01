from collections import deque
import math

input = []
with open("input2.txt") as file:
    input = [int(line.rstrip().replace("L","-").replace("R","")) for line in file]

position = 50
zeros = 0
for shift in input:
    # Handle rotations > 100
    q, r = divmod(abs(shift), 100)
    zeros += q
    effective_rotation = int(math.copysign(r, shift))
    # Handle rotations crossing the zero
    if position + effective_rotation < 0:
        if position != 0:
            zeros += 1
        position = 100 + (position + effective_rotation)
    elif position + effective_rotation > 99:
        if position != 0:
            zeros += 1
        position = position + effective_rotation - 100
    elif position + effective_rotation == 0:
        zeros += 1
        position = 0
    else:
        position = position + effective_rotation

    assert(position >= 0)

print(zeros)
