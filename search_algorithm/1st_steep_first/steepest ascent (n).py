from numeric import *

NumEval = 0    # Total number of evaluations

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): ###
    #현재(current) 좌표를 기준으로 DELTA만큼 각 variable에 대해 빼거나 더한 좌표를 neighbors에 저장후 return
    neighbors = []
    for i in range(len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors     # Return a set of successors


def bestOf(neighbors, p): ###
    #각 neighbor들에 대해 evaluate를 실행해 값 계산
    evals = []
    for neighbor in neighbors:
        evals.append(evaluate(neighbor, p))
    #가장 낮은 값이 좋은값
    bestValue = min(evals)
    #가장 낮은 값 좌표, 가장 낮은 값 담아서 return
    best = neighbors[evals.index(bestValue)]
    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
