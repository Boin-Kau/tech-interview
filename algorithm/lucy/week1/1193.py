X = int(input())
cycle = 1
while X > cycle:
    X -= cycle
    cycle += 1
if cycle % 2 == 0:
    print(f'{X}/{cycle+1-X}')
else:
    print(f'{cycle+1-X}/{X}')

# 1 -> 1/1

# 2 -> 1/2
# 3 -> 2/1

# 4 -> 3/1
# 5 -> 2/2
# 6 -> 1/3

# 7 -> 1/4
# 8 -> 2/3
# 9 -> 3/2
# 10 -> 4/1

# 11 -> 5/1