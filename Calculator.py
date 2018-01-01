# Simple calc for float's

try:
    a = float(input("Enter first number "))
    b = float(input("Enter second number "))
    # Calc
    print('a + b = ', a + b)
    print('a - b = ', a - b)
    print('a * b = ', a * b)
    if b != 0.0:
        print('a / b = ', a / b)

except:
    print('Something has gone wrong. Numbers expected')

finally:
    print('Stopped')
