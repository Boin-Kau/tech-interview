N = int(input())
W = -1
cnt = 0

while (N != W):
  if(W == -1): W = N

  x = W // 10
  y = W % 10
  W = (y * 10) + ((x + y) % 10)

  cnt += 1

print(cnt)


