T = int(input())
for i in range(T):
    cnt = 0
    ocnt = 0
    R = input()
    for o in R:
        if o == 'O':
            ocnt += 1
        else:
            ocnt = 0
        cnt += ocnt
    print(cnt)