# break statement

for i in range(10):
    if i == 7:
        print("processing is enough.. plz break")
        break
    print(i)

# This example demonstrates breaking out of a while loop when a condition is met.

count = 0

while True:
    count = count + 1
    if count >= 5:
        print("condition met")
        break
    print(count)

# This example shows breaking out of a for loop when a specific element is found

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(f"Current number: {number}")
    if number == 5:
        print("Number 5 found, breaking the loop")
        break

# This example shows breaking out of nested loops using a flag.

found = False

for i in range(5):
    for l in range(5):
        print(f"i = {i}, l = {l}")
        if i == 2 and l == 3:
            found = True
            break


    if found:
        print("we got our match")
        break






