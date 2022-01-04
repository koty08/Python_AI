import random
import math

NumEval = 0    # Total number of evaluations

def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    fileName = input("Enter the file name of a TSP: ")
    infile = open(fileName, 'r')
    # First line is number of cities
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()  # The rest of the lines are locations
    while line != '':
        locations.append(eval(line)) # Make a tuple and append
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table

def calcDistanceTable(numCities, locations):
    #도시 개수 x 도시개수 의 2차행렬 생성
    table = [[0 for col in range(numCities)] for row in range(numCities)]

    #첫번째(index 0)도시부터 이중 for문 돌려가며 다른 도시와의 거리 -> 두 점 사이 거리공식
    #루트((x2-x1)^2 + (y2-y1)^2)을 통해 table에 저장
    for i in range(numCities):
        for j in range(numCities):
            table[i][j] = math.sqrt((locations[j][0]-locations[i][0])**2 + (locations[j][1]-locations[i][1])**2)
            # print(table[i][j])

    return table # A symmetric matrix of pairwise distances

def randomInit(p):   # Return a random initial tour
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init

def evaluate(current, p):
    ## Calculate the tour cost of 'current'
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids

    #총 eval횟수 체크
    global NumEval
    NumEval += 1
    
    #만들어두었던 거리 테이블을 참조하여 한 여행에서 i번째 인덱스와 i+1번째 인덱스 사이의 거리를 for문을 돌려
    #총 거리를 구함 - 마지막 인덱스는 반복 x -> 오류
    cost = 0.0
    for i in range(len(current)-1):
        cost += p[2][current[i]][current[i+1]]
    
    return cost

def inversion(current, i, j):  ## Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print()
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

