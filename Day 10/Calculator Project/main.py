def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_operations={"+":add, "-":subtract,
                "*":multiply, "/":divide}

print(math_operations["*"](n1=4, n2=8))

