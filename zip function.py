arr3=[10,9,2,1,3]
arr1=[2,3,7,8,9]
arr2=[1,4,5,7,8]
z1=zip(arr1,arr2)
z11=list(z1)
print(z11)
z3=zip(z11,arr3)
z33=list(z3)
print(z33)
listA,listB=zip(*z33)
print(listA)
print(listB)
listc,listd=zip(*listA)
print(listc)
print(listd)
