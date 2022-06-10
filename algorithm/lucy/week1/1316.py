N = int(input())
cnt = N
for _ in range(N):
    W = input()
    for i in range(len(W)-1):
        if W[i] != W[i+1]:
            if W[i] in W[i+1:]:
                cnt -= 1
                break
print(cnt)