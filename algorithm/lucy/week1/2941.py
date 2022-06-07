c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in range(len(c)):
    a = a.replace(c[i],'a')
print(len(a))

# c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# a = input()
# for i in c:
#     a = a.replace(i,'*')
# print(len(a))