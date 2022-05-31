T = int(input())

for t in range(T):
  # k층 n호
  K = int(input())
  N = int(input())

  lst = [i for i in range(1, N+1)]
  
  for i in range(K):
    for j in range(1, N):
      lst[j] = lst[j] + lst[j-1]
  print(lst[-1])






