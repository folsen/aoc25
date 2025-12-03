input = []
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

p1 = 0
for bank in lines:
    max_jolt = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > max_jolt:
                max_jolt = joltage
    p1 += max_jolt

print(p1)
