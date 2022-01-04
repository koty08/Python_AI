import random
import math

NumEval = 0
DELTA = 0.01

def createProblem(): ###
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.

    #파일 불러온뒤 첫줄은 표현식이므로 바로 expression 변수에 저장
    filename = input("Enter the file name of a function: ")
    infile = open(filename, 'r')
    expression = infile.readline().strip()

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
    p = (expression, domain)
    return p

def randomInit(p): ###
    init = []
    #식에 사용되는 변수의 개수를 알아내기 위해 len을 사용
    var_n = len(p[1][0])

    #개수만큼 반복하여 각 변수의 최저 최고값을 알아낸뒤 random.uniform을 사용해 
    # 두 float변수 사이의 임의의 값을 받아와 init에 저장한 뒤 return
    for i in range(var_n):
        low = p[1][1][i]
        up = p[1][2][i]
        init.append(random.uniform(low, up))

    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple
