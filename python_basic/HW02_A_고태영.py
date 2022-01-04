# 입력받은 문자열을 리스트로 바꿈
inp = list(input("Enter a number as list : "))
a = []
# 그중에서 숫자만 추출하여 새 리스트 생성
for i in inp:
    if(i.isnumeric()):
        a.append(int(i))

a.sort()

#중간값 설정
mid = int(len(a)/2)
#길이가 홀수일경우 중간값 그자체
if(len(a) % 2 == 1):
    print("Median : %.1f" % float(a[mid]))
#짝수일경우 중간쪽에 위치한 두값 평균
else:
    ret = (a[mid] + a[mid-1])/2.0
    print("Median : %.1f" % ret)