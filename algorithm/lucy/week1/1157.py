W = input().upper()
S = list(set(W))
cnt = []
for i in S:
    cnt.append(W.count(i))
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(S[cnt.index(max(cnt))])