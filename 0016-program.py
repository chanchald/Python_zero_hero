# nested loop

for i in range(1,6):
    for l in range(1,6):
        print("i =",i,"l =",l)
    print()
print()

# try another

print("Try another")
for i in range(1,6):
    for l in range(1,6):
        print(f"{i*l:2}",end=" ")
    print()
print()
# this one interesting

print("This one interesting")

for i in range(1,11):
    for l in range(i):
        print("*",end=" ")
    print()
print()
# another

for i in range(10,0,-1):
    for l in range(i):
        print("*",end=" ")
    print()
print("Thank you")