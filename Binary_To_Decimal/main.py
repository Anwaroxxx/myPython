binary_str = "1101"

decimal_value = 0
power = 1

for bit in reversed(binary_str):
    if bit == '1':
        decimal_value += power
    power *= 2

print(f"Decimal value: {decimal_value}")
