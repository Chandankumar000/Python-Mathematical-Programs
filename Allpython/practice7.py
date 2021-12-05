#find circumfrence of circle FORMULA=2*PI*R
r=float(input("Enter the radius: "))
#without function
import math
pi=3.14
# cicumC=2*pi*r
# print(cicumC)

#with function
# def cir(r):
#     circumfrenceC=2*pi*r
#     return circumfrenceC
# c=cir(r)
# print(c)

#useing class
class cofc:
    def circumofc(self,r):
        a=2*pi*r
        return a

obj=cofc()
c1=obj.circumofc(r)
print(c1)