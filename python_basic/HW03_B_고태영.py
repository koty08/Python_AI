def populateDictionary():
    #파일 읽기
    f = open("Units.txt", "r")
    fdict = dict()
    while True:
        #매줄 읽기
        line = f.readline()
        if not line:
            break;
        #그줄 개행문자 제거후 , 기준 split하여 첫번째 값은 단위, 두번째값은 그 단위의 feet값을 따로 저장
        unit = line.strip().split(",")[0]
        feet = float(line.strip().split(",")[1])
        #딕셔너리에 unit값을 key로, 그 단위의 feet값을 value로 저장
        fdict[unit] = feet

    f.close()
    return fdict

def getInput():
    #사용자로부터 차례로 입력받기
    orig = input("Unit to convert from: ")
    dest = input("Unit to convert to: ")
    length = int(input("Enter length in {}s: ".format(orig)))
    return orig, dest, length


def main():
    feet = populateDictionary()
    orig, dest, length = getInput()
    #단위 변환
    ans = length * feet[orig] / feet[dest]
    #출력
    print("Length in {0}s: {1:,.4f}".format(dest, ans))

main()