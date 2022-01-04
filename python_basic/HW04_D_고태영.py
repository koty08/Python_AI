class Fraction:
    #생성자 선언
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denomiator = denominator

    #분자값 바꾸는 함수
    def setNumerator(self, numerator):
        self.numerator = numerator

    #분자값 return하는 함수
    def getNumerator(self):
        return self.numerator

    #분모값 바꾸는 함수
    def setDenominator(self, denomiator):
        self.denomiator = denomiator

    #분모값 return하는 함수
    def getDenomiator(self):
        return self.denomiator
    
    #GCD구해주는 함수
    def GCD(self, m, n):
        while n != 0:
            t = n
            n = m % n
            m = t
        return m
    
    #약분 수행하는함수
    def reduce(self):
        #GCD를 구한뒤 분자와 분모를 GCD로 둘다 나눔
        gcd = self.GCD(self.numerator, self.denomiator)
        self.numerator /= gcd
        self.denomiator /= gcd

        #나눗셈을 통해 값이 float형으로 바뀌었으니 정수형으로 다시 바꿔줌
        self.numerator = int(self.numerator)
        self.denomiator = int(self.denomiator)

def main():
    #fraction객체 생성후 사용자로부터 분자 분모 입력받음
    frac = Fraction()
    numer = int(input("Enter numerator of fraction: "))
    deno = int(input("Enter denominator of fraction: "))

    #입력받은 값을 함수를 호출하여 전달
    frac.setNumerator(numer)
    frac.setDenominator(deno)

    #약분 수행함수 호출
    frac.reduce()

    print("Reduction to lowest terms: {}/{}".format(frac.getNumerator(), frac.getDenomiator()))

main()