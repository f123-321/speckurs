s = input()
a_str = ""
b_str = ""
comma_found = False
count = 0

for char in s:
    if char == ',':
        comma_found = True
    elif not comma_found:
        a_str += char
    else:
        b_str += char

a = int(a_str)
b = int(b_str)
m = b

for i in range(a):
  if a >= b:
    count += 1
    b = b + m
  else:
    break
  
ans = a - (count * m)
print(ans)