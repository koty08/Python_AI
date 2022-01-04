#무작위 뽑기 위한 random import
import random

class Contestant:
    #생성자 정의
    def __init__(self, name="", score = 0):
        self.name = name
        self.score = score
    #이름 return하는 함수
    def getName(self):
        return self.name
    #점수 return하는 함수
    def getScore(self):
        return self.score
    #점수 늘리는 함수
    def incrementScore(self):
        self.score += 1

class Human(Contestant):
    def makeChoice(self):
        #사용자로부터 가위바위보 입력받아서 입력받은거 return
        choice = input("{}, enter your choice: ".format(self.name))
        return choice

class Computer(Contestant):
    def makeChoice(self):
        #가위바위보 리스트에서 무작위로 하나 뽑아서 출력후 return
        choice_list = ['rock', 'scissors', 'paper']
        choice = random.choice(choice_list)
        print("{} chooses {}".format(self.name, choice))
        return choice

def playGames(h, c):
    for i in range(3):
        choiceH = h.makeChoice()
        choiceC = c.makeChoice()
        if choiceH == choiceC:
            pass
        elif higher(choiceH, choiceC):
            h.incrementScore()
        else:
            c.incrementScore()
        print(h.getName() + ":", h.getScore(), c.getName() + ":", c.getScore())
        print()

def higher(c1, c2):
    if ((c1 == 'rock' and c2 == 'scissors') or
        (c1 == 'paper' and c2 == 'rock') or
        (c1 == 'scissors' and c2 == 'paper')):
        return True
    else:
        return False

def main():
    #사용자로부터 사람과 컴퓨터 이름 입력받기
    h_name = input("Enter name of human: ")
    c_name = input("Enter name of computer: ")

    #입력받은 이름으로 각각 객체 생성
    H = Human(name= h_name)
    C = Computer(name= c_name)

    #게임 함수 호출
    playGames(H, C)

    #사람의 점수가 더 높으면 사람이름 출력
    if(H.getScore() > C.getScore()):
        print("{} WINS".format(H.getName().upper()))
    #컴퓨터의 점수가 더높으면 컴퓨터이름 출력
    elif(H.getScore() < C.getScore()):
        print("{} WINS".format(C.getName().upper()))
    #두개 다아니면, 즉 동점이면 TIE출력
    else:
        print("TIE")

main()