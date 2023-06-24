a,b = map(int,input().split())
c = [0] * a
for p in range(b):
    i,j,k = list(map(int,input().split()))
    for l in range(i-1,j):
        c[l] = k
for g in range(a):
    print(c[g],end=" ")