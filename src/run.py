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
            firstNum = float(input("First number: "))
            secondNum = float(input("Second number: "))
        except ValueError:
            print("Invalid. Reenter choice.")
            continue

    if operation == '1':
        calculation = add(firstNum,secondNum)
    elif operation == '2':
        calculation = subtract(firstNum,secondNum)
    elif operation == '3':
        calculation = multiply(firstNum,secondNum)
    elif operation == '4':
        calculation = multiply(firstNum,secondNum)
       
    print(calculation)
    
    #another calculation?
    nextCalc = input("Another calculation? (yes/no)")
    if nextCalc == yes:
        previousCalc = input("Would you like to use the previous answer? (yes/no)")
        if previousCalc == yes:
            firstNum = calculation