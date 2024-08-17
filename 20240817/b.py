x = float(input())

if isinstance(x, float) and x.is_integer():
    print(int(x))
else:
    print(x)