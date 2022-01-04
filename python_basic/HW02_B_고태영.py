#4자리 수니 1000부터 9999까지 반복
for num in range(1000, 10000):
    #숫자의 각 자리수 나눠 리스트로 만듬
    li = [i for i in str(num)]
    #뒤집기
    li.reverse()
    #뒤집은 자릿수 리스트를 다시 join히여 숫자로 만듬
    new_num = int("".join(li))
    #원래 숫자의 4를 곱한값이 뒤집은 숫자와 같으면 출력
    if(4*num == new_num):
        print("Since 4 x {} is {},".format(num, new_num))
        print("the special number is {}.".format(new_num))