def all_increasing(ls):
    for l1, l2 in zip(ls, ls[1:]):
        if l1 >= l2 or abs(l1-l2) > 3:
            return False
    return True

def all_decreasing(ls):
    for l1, l2 in zip(ls, ls[1:]):
        if l1 <= l2 or abs(l1-l2) > 3:
            return False
    return True

def is_safe(report, part_two):
    levels = report.split()
    levels = [int(level) for level in levels]
    safe = all_decreasing(levels) or all_increasing(levels)
    if not safe and part_two:
        for i, v in enumerate(levels):
            tmp = levels.copy()
            del tmp[i]
            if all_decreasing(tmp) or all_increasing(tmp):
                return True

    return safe

with open("input.txt") as f:
    lines = f.read().splitlines()

c = 0
for report in lines:
    c += is_safe(report, False)
print(c)

c = 0
for report in lines:
    c += is_safe(report, True)


print(c)


