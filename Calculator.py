def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

print('Select operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

choice = input('Enter choice (1/2/3/4): ')

if choice == '1':
    print(f'{num1} + {num2} = {add(num1, num2)}')
elif choice == '2':
    print(f'{num1} - {num2} = {subtract(num1, num2)}')
elif choice == '3':
    print(f'{num1} * {num2} = {multiply(num1, num2)}')
elif choice == '4':
    try:
        print(f'{num1} / {num2} = {divide(num1, num2)}')
    except ValueError as e:
        print(e)
else:
    print('Invalid input')
