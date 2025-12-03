input = []
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]


def reduce(bank, smallest):
    for i in range(len(bank)):
        if i == len(bank) - 1 and len(bank) > 12 and int(bank[i]) in smallest:
            return bank[:i]
        elif i == len(bank) - 1:
            return bank

        if int(bank[i]) < int(bank[i + 1]):
            return bank[:i] + bank[i + 1 :]
    return bank


p2 = 0
for bank in lines:
    smallest = list(map(int, list(bank)))
    smallest.sort()
    smallest = set(smallest[: len(bank) - 12])
    while len(bank) > 12:
        bank = reduce(bank, smallest)

    p2 += int(bank)

print(p2)
