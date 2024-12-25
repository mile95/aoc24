from collections import defaultdict
from itertools import combinations, product

with open("input.txt") as f:
    sections = [s.splitlines() for s in f.read().split("\n\n")]

locks = []
keys = []
for section in sections:
    G = section
    C = len(section[0])
    curr = []
    for c, v in enumerate(zip(*G)):
        curr.append((list(v).count("#") - 1))
    if set(section[0]) == set("#"):
        locks.append(curr)
    else:
        keys.append(curr)

ans = 0
for l, k in list(product(locks, keys)):
    ans += all([(a + b) <= C for (a, b) in zip(l, k)])

print(ans)
