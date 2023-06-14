class u:

  def s():
    c = n + 1
    for i in range(n + 1):
      c = c - 1
      print(" " * (i) + "*" * c)

  def t():
    for i in range(n + 1):
      print("*" * i)

  def st():
    c = n + 1
    for i in range(1 + n):
      c = c - 1
      print(" " * c, "*" * i+ "*" * i)

  def m():
    c = n + 1
    for i in range(1, n + 2):
      print(" " * (n + 1 - i) + "*" * (i * 2 - 1))
      for i in range(1, n + 1):
        c = c - 1
        print(" " * (n + 1 - c) + "*" * (c * 2 - 1))


n = int(input("몇줄출력할건가요 :"))
a = int(input("0=직삼각형 1=삼각형 2=정삼각형 3=마름모:"))

if a == 0:
  u.s()
if a == 1:
  u.t()
if a == 2:
  u.st()
if a == 3:
  u.m()
