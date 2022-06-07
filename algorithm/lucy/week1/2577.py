A = int(input())
B = int(input())
C = int(input())
D = list(map(int, str(A*B*C)))
for i in range(10):
    print(D.count(i))