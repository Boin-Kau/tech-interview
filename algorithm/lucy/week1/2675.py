T = int(input())
for t in range(T):
    R, S = input().split()
    P =''
    for s in S:
        P += int(R)*s
    print(P)