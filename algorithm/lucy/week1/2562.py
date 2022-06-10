N = []
max = 0
p = 0
for i in range(9):
    N.append(int(input()))
    if(N[i] > max):
        max = N[i]
        p = i+1
print(max, p)