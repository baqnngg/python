#백준 단계별로 풀어보기 : 입출력과 사칙연산

#1. Hello World
print("Hello World!")

#2. A+B
a,b = map(int,input().split())
print(a+b)

#3. A-B
a,b = map(int,input().split())
print(a-b)

#4.	A*B
a,b = map(int,input().split())
print(a*b)

#5. A/B
a,b = map(int,input().split())
print(a/b)

#6. 사칙연산
a,b = map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

#7. ??!
a = input()
print(a+'??!')

#8. 1998년생인 내가 태국에서는 2541년생?!
a = int(input())
print(a-543)

#9. 나머지
a,b,c = map(int,input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#10. 곱셈
a = int(input())
b = list(map(int,input()))
print(a*b[2])
print(a*b[1])
print(a*b[0])
print(a*b[2]+a*b[1]*10+a*b[0]*100)

#11. 꼬마 정민
a,b,c = map(int,input().split())
print(a+b+c)

#12. 고양이
print('\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

#13. 개
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")