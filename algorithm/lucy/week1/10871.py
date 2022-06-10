N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
# A = [int(x) for x in input().split()]
for i in range(N):
    if (A[i] < X):
        B.append(A[i])
# 리스트 요소 한번에 출력
print(*B)

# 풀이2
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in A:
#     if i < X:
#         print(i, end=" ")
# end를 한 칸 공백으로 설정