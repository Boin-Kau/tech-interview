S = int(input())

n = 1
while(True):
  if(n*(n+1)/2 <= S < (n+1)*(n+2)/2):
    print(n)
    break
  n += 1



