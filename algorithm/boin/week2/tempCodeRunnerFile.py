T = int(input())
for t in range(T):
  # H : 호텔 층 수
  # W : 각 층의 방 수
  # N : 몇 번째 손님인지
  H, W, N = map(int, input().split())

  room = N // H + 1
  floor = N % H 
  print(floor * 100 + room)



  


