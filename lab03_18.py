import math as m
r =float(input("Input an angle in radian: "))
d =int(input("Input a distance to target: "))
v =int(input("Input a projectile velocity: "))
g = 32.17


time = d/(v*(m.cos(r)))
height = v*(m.sin(r))*time-(g*time*time/2)
print("The flight will take %.2f seconds." %time)
print("The height at impact is %.2f feet." %height)

