import time
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

def keyPress(x: str) -> bool:
    key = keyboard.isPressed(x)
    return key

i = 0
operations = ['[add] sub mul div', 'add [sub] mul div', 'add sub [mul] div', 'add sub mul [div]']
arrayValue = '0'
prevCalc = 'no'
num_1 = 0
num_2 = 0
currKeyR = False
currKeyL = False
currKeyE = False

# general start up
while True:
    time.sleep(0.5)
    while arrayValue == '0':
        print("Use your arrow keys and enter to select operation: ")

        # interface to choose operation
        while i <= 3:
            print(f'\r{operations[i]}', end="")
            prevKeyR = currKeyR
            currKeyR = keyboard.is_pressed('right')
            prevKeyL = currKeyL
            currKeyL = keyboard.is_pressed('left')
            prevKeyE = currKeyE
            currKeyE = keyboard.is_pressed('enter')
            # increment and decrement depending on key press 
            if  prevKeyR == False and currKeyR == True:
                print(f'\r{operations[i]}', end="")
                i += 1
            if prevKeyL == False and currKeyL == True:
                print(f'\r{operations[i]}', end="")
                i -= 1
            if prevKeyE == False and currKeyE == True:
                time.sleep(0.5)
                arrayValue = operations[i]
                i = 5
                
        # set operation interface to intial
        while i == 4:
            print(f'\r{operations[0]}', end="")
            i = 0
        
        # input validation & input numbers
        while i == 5:
            key1 = False
            key2 = False
            key3 = False
            time.sleep(2)
            if prevCalc == 'no' or prevCalc == 'n':
                try:
                    num_1 = float(input("\nFirst number: "))
                except ValueError:
                    print('Invalid. Restart.')
                    break
            elif prevCalc == 'yes' or prevCalc == 'y':
                num_1 = answer
            try:
                num_2 = float(input('Second number: '))            
            except ValueError:
                print('Invalid. Restart.')
                break

            # perform calculation
            if arrayValue == operations[0]:
                answer = add(num_1, num_2)
            elif arrayValue == operations[1]:
                answer = subtract(num_1, num_2)
            elif arrayValue == operations[2]:
                answer = multiply(num_1, num_2)
            elif arrayValue == operations[3]:
                if num_2 == 0:
                    print('Cannot divide by 0. Error.')
                    break
                answer = divide(num_1, num_2)

            print('Your answer is ', answer)

            # another calc?
            nextCalc = input('Another calc? (yes/no)')
            if nextCalc == 'no' or nextCalc == 'n':
                break
            prevCalc = input('Would you like to use the previous answer? (yes/no)')

    # print(f'\r{i}', end="")
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
