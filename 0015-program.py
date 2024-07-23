# while loop
# to print numbers from 1 to 10 by using while loop
print("to print numbers from 1 to 10 by using while loop")

x = 1
while x<=10:
    print(x)
    x +=1


# to display sum of first n number
print("to display sum of first n number")
n = int(input("Enter number: "))
sum = 0
x = 1
while x <= n:
    sum = sum+x
    x+=1
print("The sum of the first",n,"numbers is",sum)

# write a program to prompt user to enter some name until "chanchal"

print("write a program to prompt user to enter some name until 'chanchal'")
name = ""
while name != "chanchal":
    name = input("Enter name").lower()
print("Thanks for confirming")

