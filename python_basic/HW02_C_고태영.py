# 입력받은 문자열을 리스트로 바꿈
inp = list(input("Input list = "))
a = []
# 그중에서 숫자만 추출하여 새 리스트 생성
for i in inp:
    if(i.isnumeric()):
        a.append(int(i))

#정렬
a.sort()
#숫자(0~9)의 빈도수를 체크하는 리스트 생성
result = [[i, 0] for i in range(10)]
#리스트에서 해당 값이 나올때마다 빈도수 리스트의 값 수정
for num in a:
    result[num][1] += 1

print("Encoded list = {}".format(result))
