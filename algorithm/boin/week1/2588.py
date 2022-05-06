a = int(input())
b = int(input())

unit_hun = b//100
unit_ten = b//10 -  unit_hun*10
unit_one = b%100 - unit_ten*10

print(a*unit_one)
print(a*unit_ten)
print(a*unit_hun)
print(a*unit_one + a*unit_ten*10 + a*unit_hun*100)
