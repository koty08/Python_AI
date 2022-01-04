from problem import *
from optimizer import *

# 문제 선택하는 함수
def selectProblem():
    print("Select the problem type:")
    print("    1. Numerical Optimization")
    print("    2. TSP")
    pType = int(input("Enter the number: "))

    #입력받은 타입에따라 다른 객체 생성
    if pType == 1:
        p = Numeric()
    else:
        p = Tsp()
    #객체 생성후 바로 파일 입력받게끔 setVariables함수 호출
    p.setVariables()
    
    return p, pType

def invalid(pType, aType):
    #tsp가 선택되고, gradient descent일시
    if(pType == 2 and aType == 3):
        # 불가능하다고 출력후 바로 종료
        print("You cannot choose Gradient Descent with TSP")
        quit()

# 알고리즘 선택하는 함수
def selectAlgorithm(pType):
    print()
    print("Select the search algorithm:")
    print("    1. Steepest-Ascent")
    print("    2. First-Choice")
    print("    3. Gradient Descent")
    aType = int(input("Enter the number: "))

    #입력받은후 유효한지 검사 하기 위해 위에 정의해둔 invalid 함수 호출
    invalid(pType, aType)
    
    optimizers = { 1: 'SteepestAscent()', 2: 'FirstChoice()', 3: 'GradientDescent()'}
    alg = eval(optimizers[aType])
    alg.setVariables(aType, pType)
    return alg

def main():
    p, pType = selectProblem()
    alg = selectAlgorithm(pType)
    alg.run(p)

main()