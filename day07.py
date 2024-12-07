from itertools import product

DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

with open("input.txt") as f:
    lines = f.read().splitlines()


def solve(ops):
    res = 0
    for line in lines:
        ans, cands = line.split(":")
        ans = int(ans)
        cands = [int(c) for c in cands.split()]

        pairs = list(zip(cands, cands[1:]))
        combs = ["".join(c) for c in list(product(ops, repeat=len(pairs)))]
        for comb in combs:
            a = 0
            for i, c in enumerate(comb):
                if i == 0:
                    x, y = cands[i], cands[i + 1]
                else:
                    x, y = a, cands[i + 1]
                if c == "+":
                    a = x + y
                if c == "*":
                    a = x * y
                if c == "X":
                    a = int(str(x) + str(y))

            if a == ans:
                res += ans
                break

    return res


print(solve(["*", "+"]))
print(solve(["*", "+", "X"]))
