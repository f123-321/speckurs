s = input()
a = []
b = ""

for char in s:
  if char == ".":
    a.append(b)
    b = ""
  else:
    b += char
a.append(b)

i = len(a) - 1
while i >= 0:
  print(a[i])
  i -= 1