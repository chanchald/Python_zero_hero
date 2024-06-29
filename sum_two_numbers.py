# Program to read 2 numbers from the keyboard, print their sum, and check datatype

x = input("Enter the first number: ")
y = input("Enter the second number: ")

# Convert input to integers
i = int(x)
j = int(y)

# Print the types of the inputs and converted values
print("Type of x >>", type(x))
print("Type of y >>", type(y))
print("Type of i >>", type(i))
print("Type of j >>", type(j))

# Print the sum of the two numbers
print("The sum is >>", (i + j))
