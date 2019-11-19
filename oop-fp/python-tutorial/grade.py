N = int(input())
stds = list()
for i in range(N):
    stds.append([input(), float(input())])

scores = list(set(stds[x][1] for x in range(N)))
scores.remove(min(scores))
min_grade = min(scores)

rlt = list()
for std in stds:
    if std[1] == min_grade:
        rlt.append(std[0])
rlt.sort()
print('\n'.join(rlt))