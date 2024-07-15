# Write a program to find biggest of given three number

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>b and a>c:
    print("Biggest Number is", a)
elif b>c:
    print("Biggest Number is", b)
else:
    print("Biggest Number is", c)