# loop with else block

cart = [10, 20, 30, 40, 50]

for i in cart:
    if i > 100:
        print("Sorry we cant process this order")
        break
    print(i)
else:
    print("Congrats! you are successfully processed")

print()

# try another

items = ["apple", "banana", "cherry"]
search_item = "banana"

for item in items:
    if item == search_item:
        print(f"Item '{search_item}' found!")
        break
else:
    print(f"Item '{search_item}' not found.")
print()

# try another

count = 0

while count < 5:
    print(count)
    if count == 3:
        print("Breaking loop.")
        break
    count += 1
else:
    print("Loop completed without break.")
