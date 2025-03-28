s = input()
t = 0
o = 0

for char in s:
    if char == '0':
        t += 1
    elif char == '1':
        o += 1

if t == o:
    print("yes")
else:
    print("no")