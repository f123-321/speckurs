s = ""
while True:
    char = input()
    if not char:
        break
    s += char

side = 0
power_of_10 = 1
for i in range(len(s) - 1, -1, -1):
    digit = ord(s[i]) - ord('0')
    side += digit * power_of_10
    power_of_10 *= 10

perimeter = 4 * side
area = side * side
diagonal = side * (2**(1/2))

def format_float(num):
    integer_part = int(num)
    fractional_part = int((num - integer_part) * 100)
    if fractional_part < 10:
        return str(integer_part) + ".0" + str(fractional_part)
    else:
        return str(integer_part) + "." + str(fractional_part)

print(format_float(float(perimeter)) + ", " + format_float(float(area)) + ", " + format_float(diagonal))