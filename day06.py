import copy

with open("input.txt") as f:
    lines = f.read().splitlines()

G = lines
R = len(G)
C = len(G[0])

# find start pos
for r, _ in enumerate(G):
    for c, v in enumerate(G[r]):
        if v not in [".", "#"]:
            start = (r, c, v)

SWITCHES = {"^": ">", "v": "<", ">": "v", "<": "^"}

visited = []
r, c, d = start
while True:
    visited.append((r, c))
    if d == "^":
        rr, cc = r - 1, c
    if d == "v":
        rr, cc = r + 1, c
    if d == ">":
        rr, cc = r, c + 1
    if d == "<":
        rr, cc = r, c - 1

    if rr < 0 or rr >= R or cc < 0 or cc >= C:
        break

    if G[rr][cc] == "#":
        rr, cc = r, c
        d = SWITCHES[d]
    r = rr
    c = cc


# Part A
visited = list(set(visited))
print(len(visited))


# Part B
s = 0
for vr, vc in visited:
    G2 = copy.deepcopy(G)
    G2[vr] = G2[vr][:vc] + "#" + G[vr][vc + 1 :]
    vs = []
    r, c, d = start
    while True:
        if (r, c, d) in vs:
            s += 1
            break
        vs.append((r, c, d))

        if d == "^":
            rr, cc = r - 1, c
        if d == "v":
            rr, cc = r + 1, c
        if d == ">":
            rr, cc = r, c + 1
        if d == "<":
            rr, cc = r, c - 1

        if rr < 0 or rr >= R or cc < 0 or cc >= C:
            break

        if G2[rr][cc] == "#":
            rr, cc = r, c
            d = SWITCHES[d]
        r = rr
        c = cc

print(s)
