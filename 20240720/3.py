# TODO：全探索調べる
import itertools

n, k = map(int, input().split())
s = input()

ans = 0
for t in set(itertools.permutations(s)):
    flag = True
    for i in range(n-k+1):
        u = t[i:i+k]
        if u == u[::-1]: flag = False
    if flag: ans += 1
print(ans)
