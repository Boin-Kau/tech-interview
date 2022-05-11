def division(n):
  return n % 42

h = [int(input()) for _ in range(10)]
divisionList = list(map(division, h))

print(len(set(divisionList)))




