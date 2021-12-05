# find Quadratic Equation
import math
a=int(input("Enter values"))
b=int(input("Enter values"))
c=int(input("Enter values"))
# first calculate the discriminant of the equation
d=(b**2)-(4*a*c)
z=math.sqrt(d)
x1=(-b+z)/2*a
x2=(-b-z)/2*a
print(x1)
print(x2)