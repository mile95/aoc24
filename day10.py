from collections import defaultdict

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("input.txt") as f:
    lines = f.read().splitlines()

G = lines
R = len(G)
C = len(G[0])


def dfs_count_reachable_nines(current, nines):
    cx, cy = current
    cv = int(G[cx][cy])

    if cv == 9:
        nines.add((cx, cy))
        return

    for dx, dy in DIRECTIONS:
        nx, ny = cx + dx, cy + dy
        if (
            0 <= nx < R
            and 0 <= ny < C
            and int(G[nx][ny]) == cv + 1
            and (nx, ny) not in nines
        ):
            dfs_count_reachable_nines((nx, ny), nines)


def dfs_all_paths_to_nines(current, path):
    cx, cy = current
    cv = int(G[cx][cy])

    if cv == 9:
        return 1

    paths = 0
    for dx, dy in DIRECTIONS:
        nx, ny = cx + dx, cy + dy
        if (
            0 <= nx < R
            and 0 <= ny < C
            and int(G[nx][ny]) == cv + 1
            and (nx, ny) not in path
        ):
            paths += dfs_all_paths_to_nines((nx, ny), path + [(nx, ny)])

    return paths


count_A = 0
count_B = 0
for r, _ in enumerate(G):
    for c, v in enumerate(G[r]):
        if int(v) == 0:
            nines = set()
            dfs_count_reachable_nines((r, c), nines)
            count_A += len(nines)
            count_B += dfs_all_paths_to_nines((r, c), [(r, c)])

print(count_A)
print(count_B)
