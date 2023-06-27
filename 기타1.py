a = []
for i in range(10):
    p = int(input())
    d = p % 42
    a.append(d)

d = set(a)
print(len(d)) 