A = int(input())
B = int(input())
b1 = B//100
b2 = (B%100)//10
b3 = B%10
print(A*b3)
print(A*b2)
print(A*b1)
print(A*b3 + 10*A*b2 + 100*A*b1)