from problem import *
from setup import *

class HillClimbing(Setup):
    def __init__(self) -> None:
        super().__init__()
        self._pType = 0
        self._aType = 0

    #사용할 변수들 parameter로 받아와서 저장
    def setVariables(self, parameters):
        self._pType = parameters['pType']
        self._aType = parameters['aType']
        self._limitStuck = parameters['limitStuck']
        self._numExp = parameters['numExp']
        self._delta = parameters['delta']
        self._alpha = parameters['alpha']
        self._dx = parameters['dx']
        self._numRestart = parameters['numRestart']
    
    def displaySetting(self):
        #Hillclimbing일경우 random restart 출력
        if(1<= self._aType <= 4):
            print("Number of random restarts: {}".format(self._numRestart))
            print()
        #numeric 문제이고 gradient descent 아닌경우 delta값 출력
        if(self._pType == 1 and self._aType != 4):
            print("Mutation step size:", self._delta)
        # first choice나 stochastic알고리즘일경우 limitStuck 출력
        if(self._aType == 2 or self._aType == 3):
            print("Max evaluations with no improvement: {} iterations".format(self._limitStuck))
        #Numeric 문제이고, Gradient Descent일경우에는
        elif(self._pType == 1 and self._aType == 4):
            #alpha값과 dx값 출력
            print("Update rate:", self._alpha)
            print("Increment for calculating derivatives:", self._dx)
        #그외의 Tsp의 경우 별다른 출력 X

    def getAType(self):
        return self._aType
        
    def getNumExp(self):
        return self._numExp

    #numRestart 값만큼 run()함수를 실행해 최적의 값 store하는 함수
    def randomRestart(self, p):
        i = 1
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()
        while(i < self._numRestart):
            #마지막 아니면 numeval 초기화 시켜서 이상한값 나오지않게함
            if(i == self._numRestart-1):
                p.setNumEval(-p.getNumEval())
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()
            if(newMinimum < bestMinimum):
                bestSolution = newSolution
                bestMinimum = newMinimum
            i+=1
        p.storeResult(bestSolution, bestMinimum)

    def displayNumExp(self):
        print()
        print("Number of experiments: {}".format(self._numExp))

class SteepestAscent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        print()
        #부모 클래스의 displaySetting 호출
        super().displaySetting()

    #기존의 steepest ascent(n) 과 steepest ascent(tsp) 에서 사용한 방식대로 run 함수 정의
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of city ids
        valueC = p.evaluate(current)
        f = open('steepest.txt','w')
        while True:
            neighbors = p.mutants(current)
            (successor, valueS) = self.bestOf(neighbors, p)
            f.write(str(round(valueC, 1))+ '\n')
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        f.close()
        p.storeResult(current, valueC)
    
    def bestOf(self, neighbors, p):
        #각 neighbor들에 대해 evaluate를 실행해 값 계산
        evals = []
        for neighbor in neighbors:
            evals.append(p.evaluate(neighbor))
        #가장 낮은 값이 좋은값
        bestValue = min(evals)
        #가장 낮은 값 좌표, 가장 낮은 값 담아서 return
        best = neighbors[evals.index(bestValue)]
        return best, bestValue

class FirstChoice(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        print()
        #부모 클래스의 displaySetting 호출
        super().displaySetting()

    #기존의 first-choice (n) 과 first-choice (tsp) 에서 사용한 방식대로 run 함수 정의
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        f= open("first.txt", "w")
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            f.write(str(round(valueC, 1))+ '\n')
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        f.close()
        p.storeResult(current, valueC)
    
class GradientDescent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: Gradient Descent")
        print()
        #부모 클래스의 displaySetting 호출
        super().displaySetting()
    
    #기존의 gradient_descent 에서 사용한 방식대로 run 함수 정의
    def run(self, p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        f = open("gradient.txt", "w")
        while True:
            successor = p.takeStep(current)
            valueS = p.evaluate(successor)
            f.write(str(round(valueC, 1))+ '\n')
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        f.close()
        p.storeResult(current, valueC)

class Stochastic(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: Stochastic")
        print()
        #부모 클래스의 displaySetting 호출
        super().displaySetting()

    def run(self, p):
        #초기값 설정
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        f= open("stochastic.txt", "w")
        i = 0
        # limitstuck 한에서
        while i < self._limitStuck:
            # neighbors를 생성한후
            neighbors = p.mutants(current)
            # stochasticBest 함수 호출
            successor, valueS = self.stochasticBest(neighbors, p)
            f.write(str(round(valueC, 1))+ '\n')
            #값이 더 작으면 옮김
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        f.close()
        p.storeResult(current, valueC)

    def stochasticBest(self, neighbors, p):
        # Smaller valuse are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]

class MetaHeuristics(Setup):
    def __init__(self) -> None:
        super().__init__()
        self._pType = 0
        self._aType = 0
        self._when = 0
        self._limitEval = 0

    def setVariables(self, parameters):
        super().setVariables(parameters)
        self._pType = parameters['pType']
        self._aType = parameters['aType']
        self._delta = parameters['delta']
        self._numExp = parameters['numExp']
        self._numSample = 10
        self._limitEval = parameters['limitEval']
    
    #getter들 정의
    def getAType(self):
        return self._aType
        
    def getNumExp(self):
        return self._numExp

    def getWhenBestFound(self):
        return self._when

    def displayNumExp(self):
        print()
        print("Mutation step size:", self._delta)
        print()
        print("Number of experiments: {}".format(self._numExp))

    def displaySetting(self):
        print("Number of evaluations until termination: {0:,}".format(self._limitEval))

class SimulatedAnnealing(MetaHeuristics):
    def displaySetting(self):
        print()
        print("Search algorithm: Simulated Annealing")
        print()
        #부모 클래스의 displaySetting 호출
        super().displaySetting()
    
    def run(self, p):
        #초기 temperature 설정
        temp = self.initTemp(p)
        current = p.randomInit()
        valueC = p.evaluate(current)
        f = open("anneal.txt", "w")
        
        for i in range(self._limitEval):
            #temperature가 0이하로 가면 종료
            if temp == 0:
                break
            #언제 최저점 나오는지 담아두는 _when 변수에 계속 저장
            self._when = i+1
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            diff = valueS - valueC
            f.write(str(round(valueC, 1))+ '\n')
            # 차가 0보다 작거나 공식에 맞는 경우 위치를 그쪽으로 옮김
            if diff < 0 or math.exp(-diff/ temp) >= random.random(): 
                current = successor
                valueC = valueS
            # 차가 거의 변화가 없으면 중지
            elif abs(diff) < 0.0001:
                break
            # 루프마다 temperature 값 변경
            temp = self.tSchedule(temp)
        f.close()
        p.storeResult(current, valueC)

    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t

    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))

class GA(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._popSize = 0     # Population size
        self._uXp = 0   # Probability of swappping a locus for Xover
        self._mrF = 0   # Multiplication factor to 1/n for bit-flip mutation
        self._XR = 0    # Crossover rate for permutation code
        self._mR = 0    # Mutation rate for permutation code
        self._pC = 0    # Probability parameter for Xover
        self._pM = 0    # Probability parameter for mutation

    def setVariables(self, parameters):
        MetaHeuristics.setVariables(self, parameters)
        self._popSize = parameters['popSize']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        if self._pType == 1:
            self._pC = self._uXp
            self._pM = self._mrF
        if self._pType == 2:
            self._pC = self._XR
            self._pM = self._mR

    def displaySetting(self):
        print()
        print("Search Algorithm: Genetic Algorithm")
        print()
        MetaHeuristics.displaySetting(self)
        print()
        print("Population size:", self._popSize)
        if self._pType == 1:   # Numerical optimization
            print("Number of bits for binary encoding:", self._resolution)
            print("Swap probability for uniform crossover:", self._uXp)
            print("Multiplication factor to 1/L for bit-flip mutation:",
                  self._mrF)
        elif self._pType == 2: # TSP
            print("Crossover rate:", self._XR)
            print("Mutation rate:", self._mR)

    def run(self, p):
        popSize = self._popSize
        pop = p.initializePop(popSize)
        #초기 최고값 구하기
        current, valueC = self.evalAndFindBest(pop, p)
        i = 0
        f = open("ga.txt", "w")
        #limitEval만큼 반복
        while i < self._limitEval:
            #언제 최적의값 찾는지 체크하는 when 계속 동기화
            self._when = i + 1
            newPop=[]
            j = 0
             # 집단 크기만큼 반복
            while j < self._popSize:
                #랜덤으로 부모 2개뽑아서
                par1, par2 = self.selectParents(pop)
                #crossover
                ch1, ch2 = p.crossover(par1, par2, self._pC)
                #이후 mutation
                ch1 = p.mutation(ch1, self._pM)
                ch2 = p.mutation(ch2, self._pM)
                #mutation한걸 새집단에 추가
                newPop.extend([ch1, ch2])
                j += 2
            #새 집단 기준으로 최적의값 체크
            successor, valueS = self.evalAndFindBest(newPop, p)
            f.write(str(valueS)+"\n")
            #최적의 값 나오면 변경
            if(valueC > valueS):
                current = successor
                valueC = valueS
            #새 집단으로 집단을 변경
            pop = newPop[:]
            i += 1
        current = p.indToSol(current)
        f.close()
        p.storeResult(current, valueC)

    #최적의 값 참는 함수
    def evalAndFindBest(self, pop, p):
        best = pop[0]
        #각 ind마다 evaluation 수행
        for i in range(self._popSize):
            p.evalInd(pop[i])

        #이후 최적의 값 best에 저장
        for i in range(self._popSize):
            if best[0] > pop[i][0]:
                best = pop[i]

        bestValue = best[0]
        return best, bestValue
    
    def selectParents(self, pop):
        ind1, ind2 = self.selectTwo(pop)
        par1 = self.binaryTournament(ind1, ind2)
        ind1, ind2 == self.selectTwo(pop)
        par2 = self.binaryTournament(ind1, ind2)
        # print(par1, par2)
        return par1, par2
    
    def selectTwo(self, pop):
        popCopy = pop[:]
        random.shuffle(popCopy)
        return popCopy[0], popCopy[1]

    def binaryTournament(self, ind1, ind2):
        if ind1[0] < ind2[0]:
            return ind1
        else:
            return ind2