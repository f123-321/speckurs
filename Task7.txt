s = input()
string = ""
char = ""
comma_found = False

for c in s:
    if c == ",":
        comma_found = True
    elif not comma_found:
        string += c
    else:
        char += c

count = 0
for c in string:
    if c == char:
        count += 1
    else:
        break

print(count)

