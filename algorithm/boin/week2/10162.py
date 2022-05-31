T = int(input())

# 버튼 A는 300초
# 버튼 B는 60초
# 버튼 C는 10초

if( T < 60 ):
  if( T % 10 == 0):
    C = T // 10
    A = B = 0
    print(A, B, C)
  else: 
    print(-1)
elif( 60 <= T < 300):
  B = T // 60
  if( (T % 60) % 10 == 0 ):
    C = (T % 60) // 10
    A = 0
    print(A, B, C)
  else:
    print(-1)
elif( 300 <= T <= 10000):
  A = T // 300
  resA = T % 300
  B = resA // 60


    
310 
10 