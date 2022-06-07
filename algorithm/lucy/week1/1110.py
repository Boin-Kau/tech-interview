N = int(input())
count = 0
A = N
while True:
    if(A<10):
        A = 11*A
    elif(A%10 == 0):
        A = A//10
    else:
        A = 10*(A%10) + (A//10 + A%10)%10
    count = count+1
    if(A == N):
        break
print(count)