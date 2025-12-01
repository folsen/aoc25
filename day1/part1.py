from collections import deque

input = []
with open("input1.txt") as file:
    input = [int(line.rstrip().replace("L","-").replace("R","")) for line in file]

clicks = deque(range(100))
clicks.rotate(50)
zeros = 0
for shift in input:
    clicks.rotate(shift)
    if clicks[0] == 0:
        zeros += 1

print(zeros)
