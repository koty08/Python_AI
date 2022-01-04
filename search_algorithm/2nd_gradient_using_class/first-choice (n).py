from problem import Problem, Numeric

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement

def main():
    p = Numeric()
    p.setVariables()
    # Call the search algorithm
    firstChoice(p)
    # Show the problem and algorithm settings
    p.describeProblem()
    displaySetting(p)
    # # Report results
    p.displayResult()

def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of values
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    p.storeResult(current, valueC)

def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()
