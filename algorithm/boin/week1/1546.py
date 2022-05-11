def changeGrade(n):
  return n / max * 100

N = int(input())
h = list(map(int, input().split()))

max = h[0]
for i in h:
  if i > max:
    max = i

newGrade = list(map(changeGrade, h))
print(sum(newGrade) / N)
