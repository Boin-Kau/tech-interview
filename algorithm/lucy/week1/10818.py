N = int(input())
A = list(map(int, input().split()))
min, max = A[0], A[0]
for i in A:
    if(i < min):
        min = i
    if(i > max):
        max = i
print(min, max)

# 파이썬 내장함수
# print(min(A), max(A))