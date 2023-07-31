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
# float(num_1) = 0.0
# float(num_2) = 0.0

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
            input = keyboard.read_key()
            if input == 'right':
                time.sleep(0.5)
                print(f'\r{operations[i]}', end="")
                i += 1
            if input == 'left':
                time.sleep(0.5)
                print(f'\r{operations[i]}', end="")
                i -= 1
            if input == 'enter':
                time.sleep(0.5)
                arrayValue = operations[i]
                i = 5
                    

        while i == 4:
            print(f'\r{operations[0]}', end="")
            i = 0
        
        while i == 5:
            time.sleep(2)
            if prevCalc == 'no' or prevCalc == 'n':
                try:
                    num_1 = input("First number: ")
                except ValueError:
                    print('Invalid. Restart.')
                    break
            elif prevCalc == 'yes' or prevCalc == 'y':
                num_1 = answer
            try:
                num_2 = input('Second number: ')            
            except ValueError:
                print('Invalid. Restart.')
                break

#     # perform calculation
            if arrayValue == operations[0]:
                answer = add(float(num_1), float(num_2))
            elif arrayValue == operations[1]:
                answer = subtract(float(num_1), float(num_2))
            elif arrayValue == operations[2]:
                answer = multiply(float(num_1), float(num_2))
            elif arrayValue == operations[3]:
                if num_2 == 0:
                    print('Cannot divide by 0. Error.')
                    break
                answer = divide(float(num_1), float(num_2))

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
