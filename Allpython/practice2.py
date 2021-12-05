#Area of Rectangle
l=float(input("Enter the length: "))
b=float(input("Enter the length: "))
# #a=l*b
# #print(a)
# def areaofract(l,b):
#     Z=l*b
# print("Area of Ract: ",l*b)

class area:
     def areaofract(self,l,b):
         return l*b

obj=area()          #first obj equal to class
a=obj.areaofract(l,b)         #then obj assign  method
print(a)