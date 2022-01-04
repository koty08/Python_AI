def readSetFromFile():
    #파일 읽기
    f = open("Names.txt", 'r')
    s = set()
    lines = f.readlines()
    #개행 문자 없애고 각 줄을 셋에다 추가
    for line in lines:
        s.add(line.strip())
    
    f.close()
    return s

def inputName():
    #사용자로부터 입력받기
    n = input("Enter a first name to be included: ")
    return n

def insertSet(mySet, name):
    #기존 셋에 입력받은 값 추가
    mySet.add(name)
    #출력양식에따라 출력
    print("{} is added in Names.txt".format(name))
    return mySet

def writeToFile(modifiedSet):
    #파일 쓰기형식으로 불러옴
    f= open("Names.txt", 'w')
    #셋을 정렬하여 각 줄마다 파일 쓰기
    for word in sorted(modifiedSet):
        f.write(word+"\n")
    
    f.close()

def main():
    mySet = readSetFromFile()
    name = inputName()
    modifiedSet = insertSet(mySet, name)
    writeToFile(modifiedSet)

main()

