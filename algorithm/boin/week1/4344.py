C = int(input())
for i in range(C):
  arr = list(map(int, input().split()))
  num = arr[0]
  avg = (sum(arr) - num) / num
  
  above = 0
  # 평균 넘는 학생 비율 구하기
  for j in range(1, len(arr)):
    if(arr[j] > avg):
      above += 1
  
  result = (above/num) * 100
  print(f'{result:.3f}%')

