import numpy as np

def main():
    print("Which learning algorithm do you want to use?")
    print(" 1. Linear Regression")
    print(" 2. k-NN")
    aType = int(input("Enter the number: "))
    
    if aType == 1:
        alg = LinearRegression()
        alg._aType = 1
    elif aType == 2:
        alg = KNN()
        alg._aType = 2

    fileName = input("Enter the file name of training data: ")
    alg.setData('train', fileName)
    fileName = input("Enter the file name of test data: ")
    alg.setData('test', fileName)
    alg.buildModel()
    alg.testModel()
    alg.report()

class ML:
    def __init__(self):
        self._trainDX = np.array([]) # Feature value matrix (training data)
        self._trainDy = np.array([]) # Target column (training data)
        self._testDX = np.array([])  # Feature value matrix (test data)
        self._testDy = np.array([])  # Target column (test data)
        self._testPy = np.array([])  # Predicted values for test data
        self._rmse= 0          # Root mean squared error
        self._aType = 0        # Type of learning algoritm

    def setData(self, dtype, fileName): # set class variables
        XArray, yArray = self.createMatrices(fileName)
        if dtype == 'train':
            self._trainDX = XArray
            self._trainDy = yArray
        elif dtype == 'test':
            self._testDX = XArray
            self._testDy = yArray
            self._testPy = np.zeros(np.size(yArray)) # Initialize to all 0
            
    def createMatrices(self, fileName): # Read data from file and make arrays
        infile = open(fileName, 'r')
        XSet = []
        ySet = []
        for line in infile:
            data = [float(x) for x in line.split(',')]
            features = data[0:-1]
            target = data[-1]
            XSet.append(features)
            ySet.append(target)
        infile.close()
        XArray = np.array(XSet)
        yArray = np.array(ySet)
        return XArray, yArray

    def testModel(self):
        n = np.size(self._testDy)
        for i in range(n):
            self._testPy[i] = self.runModel(self._testDX[i])
        
    def report(self):
        n = np.size(self._testDy) # Number of test data
        totalSe = 0
        for i in range(n):
            se = (self._testDy[i] - self._testPy[i]) ** 2
            totalSe += se
        self._rmse = np.sqrt(totalSe) / n
        print()
        print("RMSE: ", round(self._rmse, 2))


class LinearRegression(ML):
    #linearRegression에 사용하는 weight 값 추가 정의
    def __init__(self):
        super().__init__()
        self._w = np.array([]) # Optimal weights for linear regression

    def buildModel(self):
        X = self._trainDX
        n = np.size(self._trainDy)
        X0 = np.ones([n, 1])
        nX = np.hstack((X0, X)) # Add a column of all 1's as the first column
        y = self._trainDy
        t_nX = np.transpose(nX)
        self._w = np.dot(np.dot(np.linalg.inv(np.dot(t_nX, nX)), t_nX), y)

    def runModel(self, data):
        nData = np.insert(data, 0, 1)
        return np.inner(self._w, nData)

class KNN(ML):
    #KNN에 사용하는 k 값 추가정의
    def __init__(self):
        super().__init__()
        self._k = 0            # k value for k-NN

    def buildModel(self):
        self._k = int(input("Enter the value for k: "))
    
    def runModel(self, query):
        closestK = self.findCK(query)
        predict = self.takeAvg(closestK)
        return predict

    def sDistance(self, dataA, dataB):
        dim = np.size(dataA)
        sumOfSqaures = 0
        for i in range(dim):
            sumOfSqaures += (dataA[i] - dataB[i]) ** 2
        return sumOfSqaures

    def findCK(self, query):
        m = np.size(self._trainDy)
        k = self._k
        #2열 K행 개의 2차원 배열 생성.
        closestK = np.arange(2 * k).reshape(k, 2)
        for i in range(k):
            closestK[i, 0] = i
            closestK[i, 1] = self.sDistance(self._trainDX[i], query)
        
        # print('closestK', closestK)
        for i in range(k, m):
            self.updateCK(closestK, i, query)
        return closestK

    def updateCK(self, closestK, i, query):
        d = self.sDistance(self._trainDX[i], query)
        # print('i', i, self._trainDX[i], 'd', d)
        for j in range(len(closestK)):
            if closestK[j, 1] > d:
                closestK[j, 0] = i
                closestK[j, 1] = d
                break
        # print('updateCK', closestK)

    def takeAvg(self, closestK):
        k = self._k
        total = 0
        for i in range(k):
            j = closestK[i, 0]
            total += self._trainDy[j]
        return total / k
    '출석체크 202055510 고태영 2021.12.09'

main()
