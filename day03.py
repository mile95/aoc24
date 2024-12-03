import re

def compute_mul(s):
    f,s = m.split('(')[1].split(',')
    s = s[:-1]
    return int(f)*int(s)

with open("input.txt") as f:
    line = f.read()

p1 = r"mul\(\d+,\d+\)"
matches = re.findall(p1, line)

ans = 0
for m in matches:
    ans += compute_mul(m)

print(ans)

p2 = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
matches = re.findall(p2, line)

ok = True
ans = 0
for m in matches:
    if m == "do()":
        ok = True
        continue
    if m == "don't()":
        ok = False
        continue

    if ok:
        ans += compute_mul(m)

print(ans)

