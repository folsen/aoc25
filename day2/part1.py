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


false_ids = []
for r in input:
    for i in r:
        if is_symmetrical(i):
            false_ids.append(i)

print(sum(false_ids))
