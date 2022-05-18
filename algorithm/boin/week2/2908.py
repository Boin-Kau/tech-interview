a, b = map(int, input().split())

newA = int(str(a)[::-1])
newB = int(str(b)[::-1])

if(newA > newB):
  print(newA)
else:
  print(newB)