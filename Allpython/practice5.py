#perimeter of ractange FORMULA=2*(L+B)

l=float(input("Enter the length: "))
b=float(input("Enter the breath: "))
# #without function
# per=2*(l+b)
# print(per)

# #with fun
# def perr(a,c):
#     return 2*(a+c)
# perrR=perr(l,b)
# print(perrR)

#useing class
class perr:
    def perrR(self,x,y):
        r=2*(x+y)
        return r
obj=perr()
c1=obj.perrR(l,b)
print(c1)
