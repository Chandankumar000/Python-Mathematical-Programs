#Find area of triangle
import math
b=float(input("Enter base: "))
h=float(input("Enter height: "))
# # l=float(input("Enter length: "))
# # # areaoftriangle=(0.5*b*h)
# # # print(areaoftriangle)
# # s=(b+h+l)/2
# # print(s)
# # a=math.sqrt(s*(s-b)*(s-h)*(s-l))
# # a=float(a)
# # print(a)
# def AOT(b,h):
#     arr=(0.5*b*h)
#     return arr
# a=AOT(b,h)
# print(a)
#useing class
class aot():
    def areaofT(self,b,h):
        return (0.5*b*h)
obj=aot()
A=obj.areaofT(b,h)
print(float(A))
