n = int(input())
a = list(map(int, input().split()))

sorted = sorted(a)

ansNo = sorted[n-2]
for i in range(n):
    if a[i] == ansNo:
        print(i+1)