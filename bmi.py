a = float(input("체중을 입력하세요 : ")) #체중을 입력받는곳
b = float(input("키를 입력하세요(1.68이런식으로) : "))   #키를 입력받습니다
c = a / (b ** 2)         #bmi 계산식
print("bmi지수는 :",round(c,2))  #bmi수치 출력
if c <= 17.33:          #저체중인지
    print("저체중")      #저체중이면 출력
elif c <= 24.95:        #정상인지
    print("정상")   
elif c <= 27.89:       #과체중인지
    print("과체중")
