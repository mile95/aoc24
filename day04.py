with open("input.txt") as f:
    lines = f.read().splitlines()


def generate_positions(start):
    result = [start]
    x, y = start
    for _ in range(1, 3):
        x += (1 if x != 0 else 0) * (1 if x > 0 else -1)
        y += (1 if y != 0 else 0) * (1 if y > 0 else -1)
        result.append((x, y))
    return result

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

ans = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        for x, y in directions:
            positions = generate_positions((x, y))
            iss = [r + a for (a, _) in positions]
            jss = [c + b for (_, b) in positions]

            if any(n < 0 for n in iss) or any(n < 0 for n in jss):
                continue

            try:
                w = (
                    lines[r][c]
                    + lines[iss[0]][jss[0]]
                    + lines[iss[1]][jss[1]]
                    + lines[iss[2]][jss[2]]
                )

                ans += w == "XMAS"
            except IndexError:
                pass

print(ans)

ans = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        try:
            if r == 0 or c == 0:
                continue
            first = lines[r - 1][c - 1] + lines[r][c] + lines[r + 1][c + 1]
            sec = lines[r + 1][c - 1] + lines[r][c] + lines[r - 1][c + 1]
            ans += (first == "MAS" or first == "SAM") and (sec == "MAS" or sec == "SAM")
        except IndexError:
            pass

print(ans)
