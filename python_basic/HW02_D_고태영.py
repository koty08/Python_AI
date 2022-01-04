def calculateValues(annualRateOfInterest, monthlyPayment, begBalance):
    #계산식에 따라 계산함 - intForMonth는 rate이므로 100으로 나눠줌
    intForMonth = annualRateOfInterest/12*begBalance/100
    redOfPrincipal = monthlyPayment-intForMonth
    endBalance = begBalance-redOfPrincipal
    #계산한 값을 tuple 형식으로 return
    return (intForMonth, redOfPrincipal, endBalance)

#함수에 필요한 값들 입력받기
aroi = int(input("annual rate of interest: "))
mp = int(input("Enter monthly payment: "))
bb = int(input("Enter beg. of month balance: "))
#return 값들을 받아와 포매팅(,구분 + 소수점 2자리까지)하여 출력
ifm, rop, eb = calculateValues(aroi, mp, bb)
print("Interest paid for the month: ${0:,.2f}".format(ifm))
print("Reduction of principal: ${0:,.2f}".format(rop))
print("End of month balance: ${0:,.2f}".format(eb))