# continue

# print odd number

for i in range(10):
    if i%2 == 0:
        continue
    print(i, end=" ")
print()

# try another

cart = [10, 20, 30, 40, 500, 50, 60]

for item in cart:
    if item == 500:
        print("wrong match")
        continue
    print(item)
print()

# try another one

numbers = [10, 5, 25, 0, 40, 0, 20]

for i in numbers:
    if i == 0:
        print("cant divided by zero")
        continue
    print("100/{} = {}".format(i, 100/i))
print()

# try another

n = [1, 2, 3, -4, 5, -6, 7]

for i in n:
    if i <= 0:
        print(f"{i} is a negative number")
        continue
    print(i)
print()
