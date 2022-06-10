import math
S = list(input())
a = S[0]
cnt = 0
for s in range(len(S)):
    if a != S[s]:
        cnt += 1
    a = S[s]
print(math.ceil(cnt/2))

# 풀이2
# cf. string도 인덱스로 접근!
# S = input()
# cnt = 0
# for s in range(len(S)-1):
#     if S[s] != S[s+1]:
#         cnt += 1
# print((cnt+1)//2)