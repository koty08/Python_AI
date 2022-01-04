from typing import NamedTuple


def displaySequenceNumbers(m,n):
    # m == n 인상황이 오면 재귀를 끝내야 하므로 그때의 m값을 return
    if(m == n):
        return m
    #이외의 경우에서는 m을 print하고 m의값을 1씩 증가시키면서 재귀함수 호출
    print(m)
    return displaySequenceNumbers(m+1, n)

def main():
    print("output of print (displaySequenceNumbers(2,4))")
    print(displaySequenceNumbers(2,4))
    print("output of print (displaySequenceNumbers(3,3))")
    print(displaySequenceNumbers(3,3))

main()