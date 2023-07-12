#add 2 numbers
def add(x, y):
    return x + y

#subtract 2 numbers
def subtract(x, y):
    return x - y

#multiply 2 numbers
def multiply(x, y):
    return x * y

#divide 2 numbers
def divide(x, y):
    return x / y

print("Which operation?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True: 
    #input operation
    operation = input("Enter operation (1/2/3/4):")

    #input validation
    if operation in ('1', '2', '3', '4'):
        try: 
            num1 = float(input("First number: "))
            secondNum = float(input("Second number: "))
        except ValueError:
            print("Invalid. Reenter choice.")
            continue

    # check options
    if operation == '1':
        calculation = add(num1,secondNum)
    elif operation == '2':
        calculation = subtract(num1,secondNum)
    elif operation == '3':
        calculation = multiply(num1,secondNum)
    elif operation == '4':
        calculation = multiply(num1,secondNum)
       
    print(calculation)
    
    #another calculation?
    nextCalc = input("Another calculation? (yes/no)")
    if nextCalc == yes:
        previousCalc = input("Would you like to use the previous answer? (yes/no)")
        if previousCalc == yes:
            num1 = calculation