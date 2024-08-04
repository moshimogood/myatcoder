a = list(map(int, input().split()))
r = list(map(int, input().split()))

t = a[1]
p = a[2]

sum = 0
for i in r:
    if i >= t:
        sum += 1

if sum >= p:
    print(0)
else:
    d =0
    while sum < p:
        d += 1
        r = list(map(lambda x: x + 1, r))
        sum = 0
        for i in r:
            if i >= t:
                sum += 1

    print(d)


