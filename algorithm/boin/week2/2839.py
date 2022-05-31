N = int(input())

# 경우의 수
# 1. N이 5로 나누어떨어지는 경우
if(N % 5 == 0):
  print(N // 5)
# 2. N을 5와 3의 조합으로 만들 수 있는 경우
# 3. 1,2번을 만족하지는 않지만, N이 3으로 나누어떨어지는 경우
else:
  cnt = 0
  while N > 0:
    N -= 3
    cnt += 1
    if(N % 5 == 0):
      print(cnt + (N//5))
      break
    elif(N == 1 or N == 2):
      print(-1)
      break
    elif(N == 0):
      print(cnt)
      break






    



