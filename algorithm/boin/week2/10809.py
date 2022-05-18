S = input()
arr = {}
count = 0

for i in S:
  if(ord(i) in arr): 
    count += 1
    continue
  else: 
    arr[ord(i)] = count
    count += 1

print(arr)

for k in range(97, 123):
  if (k in arr):
    print(arr[k], end=' ')
  else:
    print(-1, end=' ')


