T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        print(100*H + N//H)
    else:
        print(100*(N%H) + N//H+1)