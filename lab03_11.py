import math
x, y = input("Enter[#total tickets][#win tickets]:").split()
x, y = int(x), int(y)
result = x*(math.tan(math.radians(y)))
print("The object height is %.2f"%result)

