class Quizzes:
    grade_list = []
    def __init__(self, listofGrades):
        #생성자로 성적을 받아옴
        self.grade_list = listofGrades

    def average(self):
        #내림차순 정렬하여 제일 마지막 값을뺌(제일 작은값)
        self.grade_list.sort(reverse=True)
        self.grade_list.pop()

        #평균을 구하기위해 전체 합을 크기로 나눔
        return sum(self.grade_list) / len(self.grade_list)

    def __str__(self):
        #양식에 맞게 출력
        return "Quiz average: {0:.1f}".format(self.average())

def main():
    #사용자로부터 6개의 퀴즈 성적을 입력받음
    listofGrades = []
    for i in range(6):
        grade = int(input("Enter grade on quiz 1: "))
        listofGrades.append(grade)

    q = Quizzes(listofGrades)
    print(q)

main()