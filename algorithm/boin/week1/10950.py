# 테스트케이스의 개수 T를 입력받는다. 
T = int(input())
for i in range(T):
  A, B = map(int, input().split())
  print(A + B)