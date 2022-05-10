N = int(input())
arr = list(map(int, input().split()))
max = min = arr[0]

if(N == 1): print(min, max)
else:
  for i in range(1, N):
    if(max < arr[i]): max = arr[i]
    if(min > arr[i]): min = arr[i]
  print(min, max)






