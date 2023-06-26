a = []

for i in range(1,31):
    a.append(i)

for _ in range(28):
    applied = int(input())
    a.remove(applied)

print(min(a))
print(max(a))