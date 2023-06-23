a=[]
d = 1
for i in range(9):
    b = int(input())
    a.append(b)
for i in range(9):
    if a[i] == max(a):
        break
    else:
        d += 1
print(max(a))
print(d)