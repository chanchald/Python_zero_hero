# Identity operator

list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]

print(id(list1))
print(id(list2))

print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)