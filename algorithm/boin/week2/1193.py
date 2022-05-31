X = int(input())

group = 0
while(True):
  group += 1
  sum = group*(group+1) // 2
  if(X <= sum):
    break;

group_num = X - sum + group

if(group % 2 == 0):
  # 역방향
  print(f"{group_num}/{group-group_num+1}")
else: 
  # 순방향
  print(f"{group-group_num+1}/{group_num}")
