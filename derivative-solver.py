import sympy

while True:
    x = sympy.Symbol('x')

    f = input("Enter a function in terms of x: ")
    f = sympy.sympify(f)

    derivative = sympy.diff(f, x)
    derivative = str(derivative)

    second = "y"
    while (second == "y"):
        derivative = str(derivative)
        derivative = derivative.replace('**', '^')
        print("Derivative:")
        print(derivative)
        if (str(f) == "0"):
            print("")
            print("The derivative of 0 is 0.")
            print("The next derivatives are all 0.")
            break
        print("")
        
        second = input("Take the next derivative (y/n): ")
        if (second == "n"):
            break
        else:
            derivative = derivative.replace('^', '**')
            f = derivative
            derivative = sympy.diff(f, x)
    print("")
