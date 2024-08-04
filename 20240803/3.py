n,  m = map(int, input().split())
a = list(map(int, input().split()))

m_sum = sum(a)

if m_sum <= m:
    print("infinite")
else:
    ok = 0
    ng = 1000000000

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        s = 0
        for i in range(n):
            s += min(a[i], mid)
        if s <= m:
            ok = mid
        else:
            ng = mid
    
    print(ok)