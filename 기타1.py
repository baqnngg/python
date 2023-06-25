a,b = map(int,input().split())
c=[]
d=0
for i in range(1,a+1):
    c.append(i)

for p in range(b):
    i,j = list(map(int,input().split()))
    d = c[i-1]
    c[i-1] = c[j-1]
    c[j-1] = d

for i in range(a):
    print(c[i],end=" ")