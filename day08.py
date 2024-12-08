from collections import defaultdict
from itertools import combinations

with open("input.txt") as f:
    lines = f.read().splitlines()

# parsing
G = lines
R = len(G)
C = len(G[0])

d = defaultdict(list)
for r in range(R):
    for c in range(C):
        v = G[r][c]
        if v != ".":
            d[v].append((r, c))

# part A
antinodes = []
for k, v in d.items():
    pairs = list(combinations(v, 2))
    for p in pairs:
        f, s = p
        diff_y = f[0] - s[0]
        diff_x = f[1] - s[1]
        f_new = (f[0] + diff_y, f[1] + diff_x)
        s_new = (s[0] - diff_y, s[1] - diff_x)
        if 0 <= f_new[0] < C and 0 <= f_new[1] < R:
            antinodes.append(f_new)
        if 0 <= s_new[0] < C and 0 <= s_new[1] < R:
            antinodes.append(s_new)


print(len(set(antinodes)))

# part B
antinodes = []
for k, v in d.items():
    pairs = list(combinations(v, 2))
    for p in pairs:
        f, s = p
        diff_y = f[0] - s[0]
        diff_x = f[1] - s[1]
        antinodes.append(f)
        antinodes.append(s)
        while True:
            one = True  # can we continue from 1st antenna?
            two = True  # can we continue from 2nd antenna?
            f_new = (f[0] + diff_y, f[1] + diff_x)
            s_new = (s[0] - diff_y, s[1] - diff_x)
            if 0 <= f_new[0] < C and 0 <= f_new[1] < R:
                antinodes.append(f_new)
                f = f_new
            else:
                one = False
            if 0 <= s_new[0] < C and 0 <= s_new[1] < R:
                antinodes.append(s_new)
                s = s_new
            else:
                two = False

            if (not one) and (not two):
                break

print(len(set(antinodes)))


# debug
"""
for a in antinodes:
    x, y = a
    G[x] = G[x][:y] + '#' + G[x][y+1:]

for line in lines:
    print(line)
"""
