T = int(input())
A = 300
B = 60
C = 10
if T%10 == 0:
    print(T//A, (T%A)//B, ((T%A)%B)//C)
else:
    print(-1)