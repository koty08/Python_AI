from problem import Problem, Numeric

def main():
    p = Numeric()
    p.setVariables()
    # # Call the search algorithm
    steepestAscent(p)
    # # Show the problem and algorithm settings
    p.describeProblem()
    displaySetting(p)
    # # Report results
    p.displayResult()

def steepestAscent(p):
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current, valueC)

def bestOf(neighbors, p): ###
    #각 neighbor들에 대해 evaluate를 실행해 값 계산
    evals = []
    for neighbor in neighbors:
        evals.append(p.evaluate(neighbor))
    #가장 낮은 값이 좋은값
    bestValue = min(evals)
    #가장 낮은 값 좌표, 가장 낮은 값 담아서 return
    best = neighbors[evals.index(bestValue)]
    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()
