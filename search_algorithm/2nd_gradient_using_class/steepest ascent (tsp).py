from problem import Problem, Tsp

def main():
    # Create an instance of TSP
    p = Tsp()
    p.createProblem()    # 'p': [numCities, locations]
    # Call the search algorithm
    steepestAscent(p)
    # Show the problem and algorithm settings
    p.describeProblem()
    displaySetting()
    # Report results
    p.displayResult()
    
def steepestAscent(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current, valueC)

def bestOf(neighbors, p):
    #각 neighbor의 eval값 담아두는 리스트 생성
    evals = []
    #evaluate함수를 호출하여 각 neighbor data(한 코스) 의 cost를 저장
    for neighbor in neighbors:
        evals.append(p.evaluate(neighbor))
    
    #가장 작은값을 bestValue에, 그 작은 값의 neighbor data를 best에 저장후 return
    bestValue = min(evals)
    best = neighbors[evals.index(bestValue)]

    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

main()
