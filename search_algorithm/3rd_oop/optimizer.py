from problem import *
from setup import *

class HillClimbing(Setup):
    def __init__(self) -> None:
        super().__init__()

    def setVariables(self, aType, pType):
        self._pType = pType
        self._aType = aType
        #FirstChoice에서 사용하는 limitStuck 정의
        self._limitStuck = 100
    
    def displaySetting(self):
        #Numeric문제이고, SteepestAscent이거나 FirstChoice일 경우에는
        if(self._pType == 1 and (self._aType == 1 or self._aType == 2)):
            # delta값 출력
            print("Mutation step size:", self._delta)
        #Numeric 문제이고, Gradient Descent일경우에는
        elif(self._pType == 1 and self._aType == 3):
            #alpha값과 dx값 출력
            print("Update rate:", self._alpha)
            print("Increment for calculating derivatives:", self._dx)
        #그외의 Tsp의 경우 별다른 출력 X

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
        while True:
            neighbors = p.mutants(current)
            (successor, valueS) = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)
        p.describeProblem()
        self.displaySetting()
        p.displayResult()
    
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
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)
        p.describeProblem()
        self.displaySetting()
        p.displayResult()
    
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
        while True:
            successor = p.takeStep(current)
            valueS = p.evaluate(successor)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)
        p.describeProblem()
        self.displaySetting()
        p.displayResult()