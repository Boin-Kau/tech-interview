A, B, V = map(int, input().split())

day = (V-B)//(A-B)

if((V-B) % (A-B) != 0):
  day += 1

print(day)