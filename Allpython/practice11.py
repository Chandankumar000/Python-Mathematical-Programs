n=int(input("Enter the values of n: "))
#Simple Program to Display Powers of 2 upto N Terms, N defined by user
# p=n-1
# m=2**(p)
# print(f"2 power {p}: " ,m)

#Display Powers of 2 using normal Function
# def pow(n):
#     p=n-1
#     return 2**p
# pow(n)
# print(f"2's power {n-1} is:" ,pow(n))

#Using anonymous (lambda) Function
anoms = lambda x: 2 ** x
print()
for i in range(n):
    print("2 raised to the power ", i, " is ", anoms(i))