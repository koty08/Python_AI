import random
NUMBER_OF_TRIALS = 10000

def matchTwoDecks():
    # 0~51까지 52개의 숫자를 담는 리스트 생성
    deck1 = [i for i in range(52)]
    deck2 = [i for i in range(52)]

    #리스트 항목을 무작위로 섞음.
    random.shuffle(deck1)
    random.shuffle(deck2)

    #총 맞는갯수 담는 변수 선언
    numMatches = 0
    for i in range(52):
        #섞은뒤 같은 인덱스끼리 비교하여 같으면 카운트 올림
        if(deck1[i] == deck2[i]):
            numMatches+=1

    return numMatches

def main():
    totalMatches = 0

    for i in range(NUMBER_OF_TRIALS):
        totalMatches += matchTwoDecks()
    avarageMatches = totalMatches / NUMBER_OF_TRIALS

    print("Average number of matched cards: {0:.3f}".format(avarageMatches))

main()