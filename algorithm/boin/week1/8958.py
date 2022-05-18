N = int(input())

for i in range(N):
  grade = 0
  count = 1
  arr = input()
  for j in range(len(arr)):
    if(arr[j] == 'O'):
      grade += count

      if(j == len(arr)-1):
        break

      if(arr[j+1] == 'O'):
        count += 1
      else: 
        count = 1
  print(grade)







