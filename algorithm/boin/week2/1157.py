S = input()
S = S.upper()
word_list = list(set(S))
count_list = []

for i in word_list:
  count = S.count(i)
  count_list.append(count)

if count_list.count(max(count_list)) > 1:
  print('?')
else:
  print(word_list[count_list.index(max(count_list))])








