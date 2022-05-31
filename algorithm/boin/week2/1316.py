N = int(input())

result = N
for i in range(N):
  word = input()
  for j in range(len(word)-1):
    if(word[j] == word[j+1]):
      pass
    elif word[j] in word[j+1:]:
      result -= 1
      break
print(result)


    

