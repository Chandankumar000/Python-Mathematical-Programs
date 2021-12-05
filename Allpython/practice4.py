#find area of circle
#withoout fun
import math
r=float(input("enter the radius: "))
pi=3.14
# # arrofcircle=3*pi*r**2
# # print(arrofcircle)
# #with fun
# def aoc(r):
#     arr=3*pi*r**2
#     return arr
# a=aoc(r)
# print(a)
#using class
class aoc:
    def arrocicle(self,radius):
        arrofCircle=3*pi*r**2
        return arrofCircle #if here i'm using print(arrofcircle) output add none also
c=aoc()
a=c.arrocicle(r)
print(a)