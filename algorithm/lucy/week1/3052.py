N = []
for i in range(10):
    N.append(int(input())%42)
print(len(list(set(N))))