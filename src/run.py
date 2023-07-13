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


prevCalc = 'no'
num1 = 0
num2 = 0

print("Which operation?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
  #input operation
  choice = str(input("Choose which operation (1/2/3/4):"))

  #input validation & input numbers
  if choice in ('1', '2', '3', '4'):
    try:
      if prevCalc == "no":
        num1 = float(input("First number: "))
      else:
        num1 == answer
      num2 = float(input("Second number: "))
    except ValueError:
      print("Invalid. Reenter choice.")
      #continue
  else:
    print("Invalid input. Restart.")
    break
   
  #perform calculation
  if choice == '1':
    answer = add(num1, num2)
  elif choice == '2':
    answer = subtract(num1, num2)
  elif choice == '3':
    answer = multiply(num1, num2)
  elif choice == '4':
    answer = divide(num1, num2)

  print("Your answer is ", answer)

  #another calc?
  nextCalc = input("Another calc? (yes/no)")
  if nextCalc == 'yes':
    prevCalc = input("Would you like to use the previous answer? (yes/no)")
  else:
    break
