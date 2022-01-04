begin = int(input("Enter beginning salary: "))
new = begin*1.1*1.1*1.1
print("New salary: ${0:10,.2f}".format(new))
print("Change: {:.2%}".format((new-begin)/begin))