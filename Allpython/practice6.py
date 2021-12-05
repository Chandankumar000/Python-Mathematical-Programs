#perimeter of Triangle FORMULA S=A+B+C
a=float(input("Eneter first length: "))
b=float(input("Eneter second length: "))
c=float(input("Eneter third length: "))
# #without fun
# s=(a+b+c)
# print(s)

# #with fun
# def perrofT(x,y,z):
#     return (x+y+z)
# perimeterofT=perrofT(a,b,c)
# print(perimeterofT)

#useing class
class perr:
    def perrT(self,x,y,z):
        s=x+y+z
        return s
obj=perr()
c1=obj.perrT(a,b,c)
print(c1)