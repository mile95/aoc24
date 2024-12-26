from collections import defaultdict
from itertools import combinations

with open("input.txt") as f:
    lines = f.read().splitlines()


d = defaultdict(int)
stones = [int(a) for a in lines[0].split()]
for stone in stones:
    d[stone] += 1

for i in range(75):
    new_d = defaultdict(int)
    for stone in list(d.keys()):
        strstone = str(stone)
        if stone == 0:
            new_d[1] += d[stone]
        elif len(strstone) % 2 == 0:
            f, s = int(strstone[: len(strstone) // 2]), int(
                strstone[len(strstone) // 2 :]
            )
            new_d[f] += d[stone]
            new_d[s] += d[stone]
        else:
            new_d[(stone * 2024)] += d[stone]

    d = new_d
    if i == 24:
        print(sum(d.values()))

print(sum(d.values()))
