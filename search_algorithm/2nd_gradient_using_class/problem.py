import random
import math

class Problem():
    def __init__(self) -> None:
        self._solution = []
        self._value = 0
        self._numEval = 0

    # accessor
    def getNumEval(self):
        return self._numEval
    def getSolution(self):
        return self._solution
    def getValue(self):
        return self._value
    
    # mutator
    def setNumEval(self, cnt):
        self._numEval += cnt
    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value
    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))

class Numeric(Problem):
    def __init__(self) -> None:
        super().__init__()
        self._delta = 0.01
        self._domain = []
        self._expression = ""

        # gradient descent
        self._dx = 0.0001
        self._alpha = 0.01

    # accessor
    def getDelta(self):
        return self._delta
    def getDx(self):
        return self._dx
    def getAlpha(self):
        return self._alpha
    
    #gradient-descent
    def takeStep(self, current):
        #변수들의 다음 위치를 저장할 리스트 생성
        new_cur = []
        for i in range(len(current)):
            #각 변수마다 그 변수에대한 편미분을 시행하고,
            grad = self.gradient(current, i)
            # 식에 따라 다음 위치를 구한다음
            value = current[i] - (self._alpha * grad)
            # 그것이 low, up 범위 내이면 다음 위치, 아니면 기존의 값을 유지하게 한다.
            if(self.isLegal(value, i)):
                new_cur.append(value)
            else:
                new_cur.append(current[i])
    
        return new_cur
        
    
    def gradient(self, current, i):
        #편미분을 하려 한 변수만 움직여야 하므로 i(index)값을 추가로 파라미터로 받아서
        current_dx = []
        for j in range(len(current)):
            # i일때 _dx = 0.0001만큼 더해주고, 아닐경우는 그냥 둔다
            if(j == i):
                current_dx.append(current[j] + self._dx)
            else:
                current_dx.append(current[j])
        # 그뒤 식에따라 evaluate하여 미분값을 return한다.
        return (self.evaluate(current_dx) - self.evaluate(current)) / self._dx

    def isLegal(self, value, i):
        #_domain에 담겨있는 low, up 값을 읽어서
        low = self._domain[1][i]
        up = self._domain[2][i]
        #해당 value가 그 사이이면 true, 아닐경우 false를 return하게 한다.
        if(low <= value <= up):  return True;
        else:    return False;

    def setVariables(self): ###
        #파일 불러온뒤 첫줄은 표현식이므로 바로 expression 변수에 저장
        filename = input("Enter the file name of a function: ")
        infile = open(filename, 'r')
        expression = infile.readline().strip()
        self._expression = expression

        #이후 변수명, 최저, 최고값이 각 줄마다 담겨져있으므로 for문을 돌려 
        # 각 줄마다 split을 통해 알맞게 각자에 해당하는 list에 저장
        varNames, low, up = [], [], []
        for line in infile:
            varNames.append(line.split(",")[0].strip())
            low.append(int(line.split(",")[1]))
            up.append(int(line.split(",")[2]))

        #이후 domain이라는 리스트로 각 리스트를 묶어줌
        domain = [varNames, low, up]
        infile.close()

        #이후 표현식과 domain을 튜플로 만든 후 return
        self._domain = domain

    def randomInit(self): ###
        init = []
        #식에 사용되는 변수의 개수를 알아내기 위해 len을 사용
        var_n = len(self._domain[0])
        #개수만큼 반복하여 각 변수의 최저 최고값을 알아낸뒤 random.uniform을 사용해 
        # 두 float변수 사이의 임의의 값을 받아와 init에 저장한 뒤 return
        for i in range(var_n):
            low = self._domain[1][i]
            up = self._domain[2][i]
            init.append(random.uniform(low, up))

        return init    # Return a random initial point
                    # as a list of values

    def evaluate(self, current):
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        self.setNumEval(1)
        expr = self._expression         # p[0] is function expression
        varNames = self._domain[0]  # p[1] is domain
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        domain = self._domain        # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def describeProblem(self):
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 

    def displayResult(self):
        print()
        print("Solution found:")
        print(self.coordinate(self._solution))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        self.report()

    def coordinate(self, solution):
        c = [round(value, 3) for value in solution]
        return tuple(c)  # Convert the list to a tuple

    #FCHC.N
    def randomMutant(self, current): ### random하게 mutate 호출
        #DELTA random하게 뽑기위해 선언
        d_ran = [self._delta, -self._delta]
        #변수중 random하게 뽑기위해 parameter i(index)는 변수의 개수 range에서 하나 뽑게 주고,
        #d(DELTA)는 위에선언한 d_ran에서 하나 임의로 뽑게하여 mutate를 호출한뒤 값을 받아 return한다.
        return self.mutate(current, random.choice(range(len(current))), random.choice(d_ran)) # Return a random successor

    #SAHC.N
    def mutants(self, current): ###
        #현재(current) 좌표를 기준으로 DELTA만큼 각 variable에 대해 빼거나 더한 좌표를 neighbors에 저장후 return
        neighbors = []
        for i in range(len(current)):
            neighbors.append(self.mutate(current, i, self._delta))
            neighbors.append(self.mutate(current, i, -self._delta))

        return neighbors     # Return a set of successors


class Tsp(Problem):
    def __init__(self) -> None:
        super().__init__()
        self._numCities = 0
        self._locations = []
        self._table = []

    #accessor

    def createProblem(self):
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
        table = self.calcDistanceTable(numCities, locations)
        
        self._numCities = numCities
        self._locations = locations
        self._table = table

    def calcDistanceTable(self, numCities, locations):
        #도시 개수 x 도시개수 의 2차행렬 생성
        table = [[0 for col in range(numCities)] for row in range(numCities)]
        #첫번째(index 0)도시부터 이중 for문 돌려가며 다른 도시와의 거리 -> 두 점 사이 거리공식
        #루트((x2-x1)^2 + (y2-y1)^2)을 통해 table에 저장
        for i in range(numCities):
            for j in range(numCities):
                table[i][j] = math.sqrt((locations[j][0]-locations[i][0])**2 + (locations[j][1]-locations[i][1])**2)

        return table # A symmetric matrix of pairwise distances

    def randomInit(self):   # Return a random initial tour
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        self.setNumEval(1)
        #만들어두었던 거리 테이블을 참조하여 한 여행에서 i번째 인덱스와 i+1번째 인덱스 사이의 거리를 for문을 돌려
        #총 거리를 구함 - 마지막 인덱스는 반복 x -> 오류
        cost = 0.0
        for i in range(len(current)-1):
            cost += self._table[current[i]][current[i+1]]
        
        return cost

    def inversion(self, current, i, j):  ## Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describeProblem(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def displayResult(self):
        print()
        print("Best order of visits:")
        self.tenPerRow(self._solution)       # Print 10 cities per row
        print()
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        self.report()

    def tenPerRow(self, solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()

    #FCHC.Tsp
    def randomMutant(self, current): # Inversion only
        while True:
            i, j = sorted([random.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    #SAHC.Tsp
    def mutants(self, current): # Inversion only
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors