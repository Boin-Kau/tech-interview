cnt = 0

while(True):
  # 연속하는 P일 중, L일동안만 사용가능. 휴가는 V일
  L, P, V = map(int, input().split())
  if(L==P==V==0):
    break
  cnt += 1
  if( V % P > L):
    print(f"Case {cnt}: {(V // P + 1) * L}")
  else:
    print(f"Case {cnt}: {(V // P) * L + (V % P)}")






