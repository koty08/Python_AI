p = int(input("Enter purchase price: "))
s = int(input("Enter selling price: "))
print("Markup : ${}".format(float(s-p)))
print("Percentage markup: {:.1%}".format(float(s-p)/p))
print("Profit margin: {:.2%}".format(float(s-p)/s))