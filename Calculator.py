#Calculator Program in python by defining operations

n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))


print("Select Operations")
print(
    "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. Division\n")

# Giving the option to the user to choose the operation

operation = int(input("Enter choice of operation 1/2/3/4: "))


# To make operation as-per-user choices

if operation == 1:
   add=n1+n2
   print('Addition',add)
    
elif operation == 2:
    sub=n1-n2
    print('Subtractionn',sub)
elif operation == 3:
    mul=n1*n2
    print ('multiplication',mul) 
    
elif operation == 4:
    div=n1/n2
    print ('division',div) 
    
else:
    print("Invalid Input")
