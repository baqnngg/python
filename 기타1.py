a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = 0
for i in range(a):
    if b[i] == c:
        d = d+1
print(d)