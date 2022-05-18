N = int(input())
count = 0

for i in range(1, N+1):
  if(i > 99):
    first = int(str(i)[0])
    second = int(str(i)[1])
    third = int(str(i)[2])

    if((first - second) == (second - third)):
      count += 1

  else: 
    count += 1

print(count)