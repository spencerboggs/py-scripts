import math

print("")
print("       Welcome to Euler's")
print("         Method Solver!")
print("    Created by Spencer Boggs")
print("")
print("  Remember to use proper syntax")
print("  Use parenthesis for complex")
print("  fractions and fractional")
print("  expressions. Please convert")
print("  cx to c*x when entering dy/dx")
print("  Use ** for exponents (x**2)")
print("")
input("    Press [Enter] to Start")
while True:
    print("")
    e = 2.7182818284
    y = input("Enter a y value: ")
    try: float(y)
    except ValueError: y = None;
    if (y != None):
        y = float(y)
    x = input("Enter a x value: ")
    try: float(x)
    except ValueError: x = None;
    if (x != None):
        x = float(x)
    stepCount = input("Number of steps: ")
    stepSize = input("Enter step size: ")
    derivative = input('Enter dy/dx: ')
    try: eval(derivative)
    except SyntaxError: derivative = None
    if (derivative != None):
        try: eval(derivative)
        except NameError: derivative = None
        if (derivative != None):
            if (str(y)) and (str(x)) and (stepCount) and (stepSize) and (derivative):
                x = float(x)
                y = float(y)
                print('')

                for i in range(int(stepCount)):
                    m = eval(derivative)
                    print("---- Step " + str(i+1) + " ----")
                    print("Slope: " + str(m))

                    print("y - " + str(y) + " = " + str(m) + "(x - " + str(x) + ")")
                    initialEquation = (str(m) + ' * x + ' + str(eval('(-x*m)+y')))

                    x = x+float(stepSize)
                    y = eval(str(initialEquation))

                    print('Tangent Line Equation ' + str(i + 1) + ': y = ' + str(initialEquation))
                    print("Y Coordinate after " + str(i+1) + " step(s): " + str(y))
                    print("Coordinates: (" + str(x) + ", " + str(y) + ")")
                    print('')
                    if (int(i+1) < int(stepCount)):
                        a = input("Press [Enter] to go to step " + str(i+2))
                    elif (int(i+1) == int(stepCount)):
                        a = input("Press [Enter] to proceed")
                    print('')        
            else:
                print('')
                print('Unsolvable. Double check')
                print('your inputs.')
        else:
            print('')
            print('Please enter a valid')
            print('equation. Enter any')
            print('multiplication with *')
            print('Ex: cx -> c*x')
            input("Press [Enter] to proceed")
    else:
        print('')
        print('Please enter a valid')
        print('equation. Enter any')
        print('multiplication with *')
        print('Ex: cx -> c*x')
        input("Press [Enter] to proceed")
