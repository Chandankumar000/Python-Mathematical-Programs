#Calculate Simple Interest #FORMULA = P*R*T/100
import math
p=float(input("Enter principal ammount: "))
r=float(input("Enter rate if intrest: "))
t=float(input("Enter time period: "))
#without function
# SI=(p*r*t)/100
# print("Total intrest is : ",SI)

#with function
def simpleI(x,y,z):
    SI=(x*y*z)/100
    return SI
obj=simpleI(p,r,t)
print(f"Total interet is : {obj}")