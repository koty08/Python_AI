import matplotlib.pyplot as plt

#텍스트 파일로부터 데이터 뽑아오기
f = open("anneal.txt", "r")
data1 = []
for line in f:
    data1.append(float(line.strip()))
f.close()

#텍스트 파일로부터 데이터 뽑아오기
f = open("first.txt", "r")
data2 = []
for line in f:
    data2.append(float(line.strip()))
f.close()

#제목, xlabel, ylabel설정
plt.title("Search Performance (TSP-100)")
plt.xlabel("Number of Evaluations")
plt.ylabel("Tour Cost")
#두개 출력을 위해 x값을 지정해야하므로 데이터 길이만큼 1,2,3... 리스트 만들어서 그래프 출력
a = [i for i in range(1, len(data1)+1)]
b = [i for i in range(1, len(data2)+1)]
plt.plot(a, data1, b, data2)
plt.legend(['Simulated Annealing', 'First-Choice HC'])
plt.show()