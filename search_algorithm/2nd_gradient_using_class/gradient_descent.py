from problem import Problem, Numeric

def main():
    p = Numeric()
    p.setVariables()
    # # Call the search algorithm
    gradientDescent(p)
    # # Show the problem and algorithm settings
    p.describeProblem()
    displaySetting(p)
    # # Report results
    p.displayResult()

def gradientDescent(p):
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        successor = p.takeStep(current)
        valueS = p.evaluate(successor)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS

    p.storeResult(current, valueC)

def displaySetting(p):
    print()
    print("Search algorithm: Gradient descent")
    print()
    print("Alpha rate:", p.getAlpha())

main()