import math as m
w = int(input("Enter the weight of the box (kg.): "))
a = int(input("Enter the angle of the slope (degree): "))
g = 9.8
result = w*g*(m.sin(m.radians(a)))
print("The force that pushes the box downward is %.2f Newton" %result)
