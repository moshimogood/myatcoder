import itertools

n, k = map(int, input().split())
r = list(map(int, input().split()))

new = [n] * n
for i in range(n):
    new[i] = [j for j in range(1, r[i]+1)]

l = list(itertools.product(*new))

for i in l:
    if sum(i) % k == 0:
        for j in i:
            print(j, end=' ')
        print()
