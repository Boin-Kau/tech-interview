H, M = map(int, input().split())

# M에서 45를 뺀다
M -= 45
# IF M이 0보다 작아진다면, H를 1 빼고 M에 60을 더해준다. 
  # IF H를 1 뺐을 때 H가 0보다 작아진다면, H에 24를 더해준다. 

if(M < 0):
  H -= 1
  M += 60
  
  if(H < 0):
    H += 24

print(H, M)

