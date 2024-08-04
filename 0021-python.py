# del statement


x = 10
print(x)
del x
# print(x) it will give NameError


# Try another-----------------------------

my_list = ["Mango", "Berry", "Jackfruit", "Lemon", "melon", "strawberry"]
del my_list[1:3]
print(my_list)
del my_list[-1]
print(my_list)

# Try another-------------------------------

my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
del my_dict['b']

print(my_dict)

# Try another-----------------------------------
a = 10
b = 20
c = 30
del a,b,c
# print(a,b,c) It will give error

# try another------------------------------------------

nested_list = [[1,2], [3,4], [5,6], [7,8], [9,10]]
del  nested_list [3][0]
print(nested_list)

# Try another-------------------------------------------

my_lists = [1, 2, 3, 4, 5, 6]

for i in range(len(my_lists)-1, -1, -1):
    if i%2==0:
        del my_lists[i]
print(my_lists)
