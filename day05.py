from collections import defaultdict


# parsing
with open("input.txt") as f:
    lines = f.read().splitlines()

rules = lines[:lines.index("")]
updates = lines[lines.index("") + 1:]

rs = []
for rule in rules:
    l,r = [int(x) for x in rule.split('|')]
    rs.append((l,r))


# part A
valids = []
invalids = []
for update in updates:
    valid = True
    numbers = [int(n) for n in update.split(',')]
    for i, n in enumerate(numbers):
        afters = [b for (a,b) in rs if a == n]
        befores = [a for (a,b) in rs if b == n]

        for a in afters:
            if a in numbers and numbers.index(a) < i:
                valid = False

        for b in befores:
            if b in numbers and numbers.index(b) > i:
                valid = False

    if valid:
        valids.append(numbers)
    if not valid:
        invalids.append(numbers)

ans = 0
for v in valids:
    center = (len(v) - 1 ) / 2
    ans += v[int(center)]
print(ans)


# part B
dones = []
todos = invalids
while not len(todos) == 0:
    for x,invalid in enumerate(todos):
        del todos[x]
        updated = []
        for i, n in enumerate(invalid):
            new_pos = 0
            afters = [b for (a,b) in rs if a == n]
            befores = [a for (a,b) in rs if b == n]

            for j, u in enumerate(updated):
                if u in afters:
                    new_pos = j
                if u in befores:
                    new_pos = j + 1
            updated.insert(new_pos, n)

        if updated == invalid:
            dones.append(updated)
        else:
            todos.append(updated)
    

ans = 0
for v in dones:
    center = (len(v) - 1 ) / 2
    ans += v[int(center)]
print(ans)


