import keyboard 

def add(x: float, y: float) -> float:
    """
    Adds 2 numbers together
    Parameters
    ---------
    x: float
    first number to add
    
    y: float
    second number to add
    
    Returns
    ---------
    float
    'x' added to 'y'. Mathematically equivalent to 'x + y'
    """
    return x + y

def subtract(x: float, y: float) -> float:
    """
    Subtracts 2 numbers 
    Parameters
    ---------
    x: float
    first number to subtract
    
    y: float
    second number to subtract
    
    Returns
    ---------
    float
    'x' subtracted by 'y'. Mathematically equivalent to 'x - y'
    """
    return x - y

def multiply(x: float, y: float) -> float:
    """
    Multiplies 2 numbers together
    Parameters
    ---------
    x: float
    first number to multiply
    
    y: float
    second number to multiply
    
    Returns
    ---------
    float
    'x' multiplied by 'y'. Mathematically equivalent to 'x * y'
    """
    return x * y

def divide(x: float, y: float) -> float:
    """
    Divides 2 numbers 
    Parameters
    ---------
    x: float
    dividend
    
    y: float
    divisor
    
    Returns
    ---------
    float
    'x' divided by 'y'. Mathematically equivalent to 'x / y'
    """
    return x / y

# variable definitions
prevCalc = 'no'
num1 = 0
num2 = 0
choice = 'none'
addVar = '[add]'
subVar = 'sub'
mulVar = 'mul'
divVar = 'div'
addArr = ['\r[add] ', '\radd ']
subArr = ['[sub] ', 'sub ']
mulArr = ['[mul] ', 'mul ']
divArr = ['[div]', 'div ']
arrayValue = 1

# general start up
def optionPicker(w, x, y, z):
    print('Which operation?')
    print(w, end='')
    print(x, end='')
    print(y, end='')
    print(z, end='')
    

# while (arrayValue == 0):
# optionPicker(addArr[0], subArr[1], mulArr[1], divArr[1])
# arrayValue = 1
# if arrayValue <= 4:
#     if keyboard.is_pressed('right'):
#         optionPicker(addArr[1], subArr[0], mulArr[1], divArr[1])
#         arrayValue += 1
#         if keyboard.is_pressed('right'):
#             optionPicker(addArr[1], subArr[1], mulArr[0], divArr[1])
#             arrayValue += 1
#             if keyboard.is_pressed('right'):
#                 optionPicker(addArr[1], subArr[1], mulArr[1], divArr[0])
#                 arrayValue += 1
# else: 
#     arrayValue = 1
    
        # input("hi: ")
# elif arrayValue > 2: 
    # elif keyboard.is_pressed('right')



while True:
    # input operation
   # options()
    choice = input('Choose which operation (1/2/3/4):')

    # input validation & input numbers
    if choice not in ('1', '2', '3', '4'):
        print('Invalid input. Restart.')
        break

    if prevCalc == 'no' or prevCalc == 'n':
        try:
            num1 = float(input('First number: '))
        except ValueError:
            print('Invalid. Restart.')
            break
    elif prevCalc == 'yes' or prevCalc == 'y':
        num1 = answer
    try:
        num2 = float(input('Second number: '))
    except ValueError:
        print('Invalid. Restart.')
        break
   
    # perform calculation
    if choice == '1':
        answer = add(num1, num2)
    elif choice == '2':
        answer = subtract(num1, num2)
    elif choice == '3':
        answer = multiply(num1, num2)
    elif choice == '4':
        if num2 == 0:
            print('Cannot divide by 0. Error.')
            break
        answer = divide(num1, num2)

    print('Your answer is ', answer)

    # another calc?
    nextCalc = input('Another calc? (yes/no)')
    if nextCalc == 'no' or nextCalc == 'n':
        break
    prevCalc = input('Would you like to use the previous answer? (yes/no)')

'''
while True:
    if keyboard.is_pressed('right'):
        print("Dear John")
        break
'''