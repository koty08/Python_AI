from tsp import *

def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': [numCities, locations]
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def steepestAscent(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS

    return current, valueC

def mutants(current, p): # Inversion only
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = inversion(current, i, j)
            count += 1
            neighbors.append(curCopy)
    return neighbors

def bestOf(neighbors, p):
    #각 neighbor의 eval값 담아두는 리스트 생성
    evals = []
    #evaluate함수를 호출하여 각 neighbor data(한 코스) 의 cost를 저장
    for neighbor in neighbors:
        evals.append(evaluate(neighbor, p))
    
    #가장 작은값을 bestValue에, 그 작은 값의 neighbor data를 best에 저장후 return
    bestValue = min(evals)
    best = neighbors[evals.index(bestValue)]

    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

main()
