A = int(input())
B = int(input())
C = int(input())
mul = str(A * B * C)
countList = [0 for i in range(10)]

for i in str(mul):
  countList[int(i)] += 1

for i in countList:
  print(i)
