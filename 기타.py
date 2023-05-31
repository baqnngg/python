while 1:
    a = int(input('마름모를 출력하려면 0 직삼각형을 출력하려면 1을 입력하세요.'))

    def 마름모():
        n = int(input())
        c = n+1
        for i in range(1,n+2):
            print(" "*(n+1-i)+"*"*(i*2-1))
        for i in range(1,n+1):
            c = c - 1
            print(" "*(n+1-c)+"*"*(c*2-1))

    def 직삼각형():
        n = int(input())
        c = n+1
        for i in range(n+1):
            c = c-1
            print(" "*(i)+"*"*c)

    if a == 0:
        마름모()
    elif a == 1:
        직삼각형()
        break