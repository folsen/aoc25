from textwrap import wrap

input = []
with open("input.txt") as file:
    line = [line.rstrip() for line in file][0]
    input = [
        range(int(r.split("-")[0]), int(r.split("-")[1]) + 1) for r in line.split(",")
    ]


def is_symmetrical(i):
    s = str(i)
    if len(s) % 2 != 0:
        return False
    if s[: len(s) // 2] == s[len(s) // 2 :]:
        return True
    else:
        return False


def is_repeating(i):
    s = str(i)
    for l in range(1, len(s) // 2 + 2):
        chunks = wrap(s, l)
        if len(chunks) > 1 and len(set(chunks)) == 1:
            return True
    return False


# Part 1
# false_ids = []
# for r in input:
#     for i in r:
#         if is_symmetrical(i):
#             false_ids.append(i)

# print(sum(false_ids))

# Part 2
false_ids = []
for r in input:
    for i in r:
        if is_repeating(i):
            false_ids.append(i)
print(sum(false_ids))
