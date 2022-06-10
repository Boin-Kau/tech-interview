n = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    n += 1
    if V%P > L:
        print(f"Case {n}: {(V//P)*L + L}")
    else:
        print(f"Case {n}: {(V//P)*L + V%P}")