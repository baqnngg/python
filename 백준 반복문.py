#백준 반복문

#1. 구구단
a=int(input())
for i in range(1,10):
    print(a,"*",i,"=",a*i)

#2. A+B - 3
a = int(input())
for i in range(a):
    c,d = map(int,input().split())
    print(c+d)

#3. 합
a = int(input())
n = 0
for i in range(1,a+1):
    n = n + i
print(n)

#4. 영수증
a = int(input())
b = int(input())
c = []
d = 0
for i in range(b):
    c.append(list(map(int,input().split())))
for i in range(b):
    d = c[i][0] * c[i][1] + d
if d == a:
    print("Yes")
else:
    print("No")

#5. 코딩은 체육과목 입니다 
a = int(input())
b = int(a/4)
for i in range(b):
    print('long', end=' ')
print("int")

#6. 빠른 A+B
import sys
T = int(input())
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

#7. A+B - 7
T = int(input())
b=[]
for i in range(T):
    b.append(list(map(int,input().split())))
for j in range(T):
    print("Case #"+str(j+1)+":",b[j][0]+b[j][1])

#8. A+B - 8
T = int(input())
b=[]
for i in range(T):
    b.append(list(map(int,input().split())))
for j in range(T):
    print("Case #"+str(j+1)+":",b[j][0],"+",b[j][1],"=",b[j][0]+b[j][1])

#9. 별 찍기 - 1
a = int(input())
for i in range(1,a+1):
    print("*"*i)

#10. 별 찍기 - 2
a = int(input())
c = a
for i in range(1,a+1):
    c = c-1  
    print(" "*c +"*"*i)

#11. A+B - 5
while 1:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)

#12. A+B - 4
while 1:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break