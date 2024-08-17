a, b, c = map(int, input().split())

if b > c:
    b -= 24

if b < a and a < c:
    print('No')
else:
    print('Yes')
