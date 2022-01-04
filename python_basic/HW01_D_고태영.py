coef = float(input("Enter coefficient of restitution: "))
height = int(input("Enter initial height in meters: "))
height *= 100
init = height

bounce = 0
traveled = 0.0
while(height > 10):
    bounce += 1
    traveled += height
    height *= coef

print("Number of bounces: {}".format(bounce))
print("Meters traveled: {:.2f}".format((traveled*2-init)/100))