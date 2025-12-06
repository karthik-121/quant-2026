def square(x):
    return x**2

def cubed(x):
    return x**3

def evaluate(f, value):
    return f(value)

number = evaluate(square, 3)
second_number = evaluate(cubed, 3)
print(number)
print(second_number)
