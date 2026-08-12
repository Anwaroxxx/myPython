def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def apply_operation(func, x, y):
    return func(x, y)


result_add = apply_operation(add, 5, 3)
result_mul = apply_operation(multiply, 5, 3)

print(f"Addition Result: {result_add}")
print(f"Multiplication Result: {result_mul}")
