# continue

# to print odd numbers in the range 0 to9
for i in range(10):
    if i%2==0:
        continue
    print(i)
print()
# try another
cart = [10, 50, 100, 155, 200, 300]

for item in cart:
    if item==155:
        print(f"we can't process this item {item}")
        continue
    print(item)
print()

# try another
numbers = [5, 10, 15, 0, 25, 30, 0, 40]

for n in numbers:
    if n == 0:
        print("can't divide with zero")
        continue
    print("100/{} = {}".format(n, 100/n))
print()

# try another

Asia = ["India", "Japan", "China", "South Korea", "France", "North Korea"]

for Country in Asia:
    if Country == "France":
        print("France is not in Asia")
        continue
    print(Country)
print()

# try another one

positive = [1, 2, 3, -4, 5, -6, 7, 8]

for n in positive:
    if n < 0:
        print(f"{n} is a negative number")
        continue
    print(n)



