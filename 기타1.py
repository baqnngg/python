a, b = map(int, input().split())

basket = [i for i in range(1,a+1)]

for i in range(b):
    i,j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for i in range(a):
    print(basket[i], end = ' ')