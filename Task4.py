def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal

def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal
    
s = input()

is_negative = False
if s[0] == '-':
  is_negative = True
  s = s[1:]

is_valid = True
for char in s:
    if not '0' <= char <= '9':
        is_valid = False
        break

if not is_valid or is_negative or not s:
    print("Неверный ввод")
else:
    decimal = 0
    for char in s:
        decimal = decimal * 10 + (ord(char) - ord('0'))

    binary = decimal_to_binary(decimal)
    octal = decimal_to_octal(decimal)
    hexadecimal = decimal_to_hexadecimal(decimal)

    print(binary + ", " + octal + ", " + hexadecimal)