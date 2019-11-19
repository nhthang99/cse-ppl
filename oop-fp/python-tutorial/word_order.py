n = int(input())
d = dict()
for i in range(n):
    line = input()
    if d.get(line):
        d[line] = d.get(line) + 1
    else:
        d[line] = 1
print(len(d))
for key in d:
    print(d[key], end=' ')