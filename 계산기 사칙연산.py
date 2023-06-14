class calculator:#클래스씀

  def plus():#더하는곳
    print(a + b)

  def minus():#빼는곳
    print(a - b)

  def multiply():#곱하는곳
    print(a * b)

  def divide():#나누는곳
    print(a / b)


a, b = map(int, input("두 수를 입력하세요 : ").split())#두수를 정수로 입력받는곳
c = input("계산할 방식을 설정해 주세요 : ")#계산방식을 받는곳

if c == "+":#c가 +일경우 밑에있는거 실행
  calculator.plus()
elif c == "-":#c가 -일경우 밑에있는거 실행
  calculator.minus()
elif c == "*":#c가 *일경우 밑에있는거 실행
  calculator.multiply()
elif c == "/":#c가 /일경우 밑에있는거 실행
  calculator.divide()
