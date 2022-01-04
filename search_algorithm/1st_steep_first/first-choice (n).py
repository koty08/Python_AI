import random
from numeric import *

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomMutant(current, p): ### random하게 mutate 호출
    #DELTA random하게 뽑기위해 선언
    d_ran = [DELTA, -DELTA]
    #변수중 random하게 뽑기위해 parameter i(index)는 변수의 개수 range에서 하나 뽑게 주고,
    #d(DELTA)는 위에선언한 d_ran에서 하나 임의로 뽑게하여 mutate를 호출한뒤 값을 받아 return한다.
    return mutate(current, random.choice(range(len(current))), random.choice(d_ran), p) # Return a random successor

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
