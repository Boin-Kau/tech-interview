num = set(range(1, 10001))
generate_num = set()

for i in num:
    for j in str(i):
        i += int(j)
    generate_num.add(i)

self_num = num - generate_num
for s in sorted(self_num):
    print(s)