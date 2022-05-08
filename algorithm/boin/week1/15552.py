# 빠른 A+B
# input 대신 sys.stdin.readline으로 입력받자

import sys


T = int(sys.stdin.readline())
for i in range(T):
  A, B = map(int, sys.stdin.readline().split())
  print(A+B)