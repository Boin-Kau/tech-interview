N = int(input())
honey = 1
cnt = 1
while N > honey:
    honey += 6*cnt
    cnt += 1
print(cnt)