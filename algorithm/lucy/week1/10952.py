while(1):
    A, B = map(int, input().split())
    if((A, B) == (0, 0)):
        break
    print(A+B)