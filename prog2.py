# How to read multiple values from the key board in a single line

a, b = [int(x) for x in input("Enter two numbers: ").split(',')]
print("Product is:", a * b)
