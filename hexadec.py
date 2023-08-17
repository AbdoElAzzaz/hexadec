def hex(num):
    hexadecimal = ""
    hex_digits = "0123456789abcdef"
    if num < 0:
        num += 2 ** 32

    while num > 0:
        remainder = num % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        num //= 16

    return hexadecimal

num = (hex(int(input("Enter the number: "))))
print(num)