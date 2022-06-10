S = input()
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
for j in alphabet:
    if j in S:
        print(S.index(j), end =' ')
    else:
        print(-1, end = ' ')

# 풀이2
# S = input()
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for x in alphabet:
#     print(S.find(x), end = ' ')