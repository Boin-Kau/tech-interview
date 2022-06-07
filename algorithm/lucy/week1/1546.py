N = int(input())
S = list(map(int, input().split()))
M = max(S)
for i in range(N):
    S[i] = S[i]/M*100
print(sum(S)/N)