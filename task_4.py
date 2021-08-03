number = int(input())

amount_digits = len(str(number)) - 1
digit = 0

while amount_digits > 0:

    if digit < (number // 10 ** amount_digits):
        digit = number // 10 ** amount_digits

    number = number % 10 ** amount_digits
    amount_digits -= 1

print(digit)
