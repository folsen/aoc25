ranges = []
ids = []
with open("input.txt") as file:
    parsing_ranges = True
    for line in file:
        if line.rstrip() == "":
            parsing_ranges = False
            continue
        if parsing_ranges:
            start, end = list(map(int, line.rstrip().split("-")))
            ranges.append((start, end))
        else:
            ids.append(int(line.rstrip()))

# P1
is_fresh = 0
for id in ids:
    for start, end in ranges:
        if id >= start and id <= end:
            is_fresh += 1
            break

print("P1:", is_fresh)

# P2
# Figure out if ranges are overlapping, if so combine them into one expanded
# range to condense the number of ranges. Should then end up with all disjoint
# ranges and be able to calculate count from there

# We need to sort the list first so we can make sure we don't need to backtrack
# and add the ranges in expanding order
ranges.sort(key=lambda e: e[0])
i = 0
while i < len(ranges):
    j = i + 1
    while j < len(ranges):
        s1, e1 = ranges[i]
        s2, e2 = ranges[j]
        ns, ne = (s1, e1)
        overlapping = False
        # Right border is expanding (we don't need to look left because sorted the list)
        if e2 > e1 and s2 <= e1:
            overlapping = True
            ne = e2
        # This is a strict subset, remove it
        if s2 >= s1 and e2 <= e1:
            overlapping = True
        # Update range i, remove range j
        if overlapping:
            ranges[i] = (ns, ne)
            ranges = ranges[:j] + ranges[j + 1 :]
        else:
            j += 1
    i += 1

p2 = 0
for s, e in ranges:
    p2 += e - s + 1

print("P2:", p2)
