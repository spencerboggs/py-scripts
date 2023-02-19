import math

print("")
print("      Welcome to Quadratic")
print("         Formula Solver!")
print("    Created by Spencer Boggs")
print("")
print("  Make sure to use the correct")
print("  variables.")
print("  Equation: ax^2 + bx + c")
print("")
print("")
input("    Press [Enter] to Start")
while True:
    negativeInSqrt = False
    print('')
    a = input("Enter a: ")
    if (float(a) != 0):
        b = input("Enter b: ")
        c = input("Enter c: ")
        print('')
        if (a) and (b) and (c):
            a = float(a)
            b = float(b)
            c = float(c)

            print("Equation: (-" + str(b) + " +- sqrt(" + str(b) + "^2 - 4(" + str(a) + ")(" + str(c) + ")))/2(" + str(a) + ")")

            try: math.sqrt((b**2) - 4 * a * c)
            except ValueError: negativeInSqrt = True

            if (negativeInSqrt != True):
                solvedSqrt = math.sqrt((b**2) - 4 * a * c)
            else:
                negativeValue = (abs((b**2) - 4 * a * c))
                solvedSqrt = "i*sqrt(" + str(negativeValue) + ")"

            if (negativeInSqrt != True):
                posAnswer = -b + solvedSqrt
                print("Plus Sqrt: " + str(posAnswer/(2 * a)))
                negAnswer = -b - solvedSqrt
                print("Minus Sqrt: " + str(negAnswer/(2 * a)))
            else:
                positiveNumerator = "-" + str(b) + " + " + str(solvedSqrt)
                print("Plus Sqrt: (" + str(positiveNumerator) + ")/" + str(2 * a))
                negativeNumerator = "-" + str(b) + " - " + str(solvedSqrt)
                print("Minus Sqrt: (" + str(negativeNumerator) + ")/" + str(2 * a))
            
        else:
            print("Please enter valid")
            print("variables")                    
    else:
        print("a cannot be 0. Please")
        print("try again")
