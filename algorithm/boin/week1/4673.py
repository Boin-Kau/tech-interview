natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
  for k in str(i):
    i += int(k)
  generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for j in self_num:
  print(j)

