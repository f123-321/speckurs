s = input()
a_str = ""
b_str = ""
c_str = ""
space_count = 0

for char in s:
    if char == ' ':
        space_count += 1
    elif space_count == 0:
        a_str += char
    elif space_count == 1:
        b_str += char
    else:
        c_str += char

a = 0
sign = 1
if a_str[0] == '-':
  sign = -1
  a_str = a_str[1:]

for char in a_str:
    a = a * 10 + (ord(char) - ord('0'))
a *= sign


b = 0
sign = 1
if b_str[0] == '-':
  sign = -1
  b_str = b_str[1:]
for char in b_str:
    b = b * 10 + (ord(char) - ord('0'))
b *= sign

c = 0
sign = 1
if c_str[0] == '-':
  sign = -1
  c_str = c_str[1:]
for char in c_str:
    c = c * 10 + (ord(char) - ord('0'))
c *= sign

if (a <= b <= c) or (c <= b <= a):
    print(b)
elif (b <= a <= c) or (c <= a <= b):
    print(a)
else:
    print(c)