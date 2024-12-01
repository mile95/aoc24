from collections import Counter

with open("input.txt") as f:
    lines = f.read().splitlines()

lefts = []
rights = []
for line in lines:
    l, r = line.split()
    lefts.append(int(l))
    rights.append(int(r))

lefts.sort()
rights.sort()

s = 0
for l, r in zip(lefts,rights):
    s += abs(l - r)
print(s)


counter = Counter(rights)
s = 0
for l in lefts:
    s += l * counter[l] 
print(s)

