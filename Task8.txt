s = input()
result = ""
word = ""

for char in s:
    if char == " ":
        if word:
            result += word[-1]
            word = ""
    else:
        word += char

if word:
    result += word[-1]

print(result)