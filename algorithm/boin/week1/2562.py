arr = [int(input()) for _ in range(9)]
max = arr[0]
index = 0

for i in range(1, 9):
  if(max < arr[i]):
    max = arr[i]
    index = i

print(max)
print(index+1)

