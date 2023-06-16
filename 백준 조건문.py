#1. 두 수 비교하기
a,b = map(int,input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')

#2. 시험성적
a = int(input())
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')

#3. 윤년
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
    print('1') 
else:
    print('0')

#4. 사분면 고르기
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")

#5. 알람 시계
a,b = map(int,input().split())
c = a*60 + b
m = c + 1395
if m >= 1440:
    m = m-1440
l = m/60
l = int(l)
print(l,m%60)

#6. 오븐 시계
a, b = map(int,input().split())
c = int(input())
m = a*60+b+c
if m >= 1440:
    m = m-1440
l = m/60
l=int(l)
if l == 24:
    l = 0
print(l, m%60)

#7. 주사위 세개
dice1,dice2,dice3 = map(int,input().split())
if (dice1 == dice2 == dice3) :
    print(10000+dice1*1000)
elif (dice1 == dice2 or dice1 == dice3) :
    print(1000+dice1*100)
elif (dice2 == dice3) :
    print(1000+dice2*100)
elif (dice1 > dice2 and dice1 > dice3) :
    print(100*dice1)
elif (dice2 > dice1 and dice2 > dice3) :
    print(100*dice2)
else :
    print(100*dice3)