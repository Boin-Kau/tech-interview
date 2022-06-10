N = int(input())
cnt = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif num[1]-num[0] == num[2]-num[1]:
        cnt += 1
print(cnt)