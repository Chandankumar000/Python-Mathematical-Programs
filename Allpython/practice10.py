# Find Union Intersection Symmetric Difference of Sets
"""
Find Union of Sets                  unionSet = setOne | setTwo
Find Intersection of Sets             intersectionSet = setOne & setTwo
Find Difference of Sets                    diffSet = setOne - setTwo
Find Symmetric Difference of Sets       symDiffSet = setOne ^ setTwo
"""
# if two set given
A={1,2,3,4,5}
B={3,4,5,6,7}
x=A.union(B)                       #union of two set
y=A.intersection(B)                #intersection of two set
z=A.difference(B)                  #difference of two set
z1=B.difference(A)
p=A.symmetric_difference(B)        #symmetric difference b/w two set
print(f"A union B is: {x}")
print(f"A intersection B is: {y}")
print(f"A difference B is: {z}")
print(f"B difference A is: {z1}")
print(f"A symmetric difference B is: {p}")

# 2nd set define run time user
###########################################UNION#############
# print("Enter 5 Elements for Set A: ")
# setOne = []
# for i in range(5):
#     setOne.append(input())
# setOne = set(setOne)
#
# print("Enter 5 Elements for Set B: ")
# setTwo = []
# for i in range(5):
#     setTwo.append(input())
# setTwo = set(setTwo)
#
# print("\nUnion of Two Sets A and B are:")
# print(setOne | setTwo)

#####################################INTERSECTION##############################

