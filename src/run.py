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

previousCalc = 'no'

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
          if previousCalc == 'yes':
            num1 = calc
          else:
            num1 = float(input("First number: "))
          secondNum = float(input("Second number: "))
        except ValueError:
            print("Invalid. Reenter choice.")
            continue

    # check options
    if operation == '1':
        calc = add(num1, secondNum)
    elif operation == '2':
        calc = subtract(num1, secondNum)
    elif operation == '3':
        calc = multiply(num1, secondNum)
    elif operation == '4':
        calc = multiply(num1, secondNum)
       
    print(calc)
    
    #another calc?
    nextCalc = input("Another calc? (yes/no)")
    if nextCalc == 'yes':
        previousCalc = input("Would you like to use the previous answer? (yes/no)")
    else:
      break