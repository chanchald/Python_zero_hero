eno = int(input("Enter Employee no: "))
ename = input("Enter Employee Name: ")
esal = float(input("Enter Employment Salary: "))
eaddr = input("Enter Employment Address: ")
married_input = input("Employee Married? [True|False]: ")
married = married_input.lower() in ['true', '1', 't', 'yes', 'y']  # Convert the input to a boolean

print("Please confirm information")
print("Employee No:", eno)
print("Employee Name:", ename)
print("Employee Salary:", esal)
print("Employee Address:", eaddr)
print("Employee Married?:", married)
