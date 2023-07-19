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
i = 0
operations = ['[add] sub mul div', 'add [sub] mul div', 'add sub [mul] div', 'add sub mul [div]']
arrayValue = '0'
prevCalc = 'no'

# while True:
#     # print(f'\r{i}', end="")
#     print(f'\r{options[0]}', end="")
#     time.sleep(2)
#     print(f'\r{options[1]}', end="")
#     time.sleep(2)
#     print(f'\r{options[2]}', end="")
#     time.sleep(2)
#     print(f'\r{options[3]}', end="")
#     time.sleep(2)
#     i += 1
while True:
    while arrayValue == '0':
        while i <= 3:
            print(f'\r{operations[i]}', end="")
            if keyboard.read_key('right'):
                time.sleep(0.1)
                print(f'\r{operations[i]}', end="")
                i += 1
            if keyboard.read_key('left'):
                time.sleep(0.1)
                print(f'\r{operations[i]}', end="")
                i -= 1
            if keyboard.read_key('enter'):
                time.sleep(0.1)
                arrayValue = operations[i]
                i = 5
                    

        while i == 4:
            print(f'\r{operations[0]}', end="")
            i = 0
        
        while i == 5:
            time.sleep(2)
            # if choice not in ('1', '2', '3', '4'):
            # print('Invalid input. Restart.')
            # break
            #if prevCalc == 'no' or prevCalc == 'n':
            try:
                num1 = float(input('\nFirst number: '))
                print('done')
            except ValueError:
                print('Invalid. Restart.')
                break
            #elif prevCalc == 'yes' or prevCalc == 'y':
                #num1 = answer
            try:
                num2 = float(input('Second number: '))
            except ValueError:
                print('Invalid. Restart.')
                break

#     # perform calculation
            if arrayValue == operations[0]:
                answer = add(num1, num2)
            elif arrayValue == operations[1]:
                answer = subtract(num1, num2)
            elif arrayValue == operations[2]:
                answer = multiply(num1, num2)
            elif arrayValue == operations[3]:
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

    # # print(f'\r{i}', end="")
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
    # print(f'\r{options[i]}', end="")
    # time.sleep(2)
