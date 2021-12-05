# Find Area of Square

# a=float(input("Enter the length: "))
# # areaofsquare=a*a
# # print(areaofsquare)
# def area(a):
#     return a*a
# print(area(a))

# class area:
#     def __init__(self,a):
#         self.a=a
#         return a*a
# #     def areaofsquare(self):
# #         return (self.a*self.a)
# # c1=area.areaofsquare(9)
# # print(c1)
# print(area(9))

class area:
    def areaofsquare(self,s):
        return s*s

#print("enter the side length: ")
L=float(input("enter the side length: "))
obj=area()
a=obj.areaofsquare(L)
print(a)
