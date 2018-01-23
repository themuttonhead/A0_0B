#to_compare_the_perimeter
a=float(input("enter the radius of circle A:"))
b=float(input("enter the radius of circle B:"))
c=float(input("enter the radius of circle C:"))
d=2*3.14*a
e=2*3.14*b
f=2*3.14*c
if d>e>f:
    print("A has bigger perimeter",d)
elif d>e==f:
    print("A has bigger perimeter")
    print("B&C have same perimeter",e)
elif e>d>f:
    print("B has bigger perimeter",e)
elif e>d==f:
    print("B has bigger perimeter",e)
    print("C&A have same perimeter",f)
elif f>d>e:
    print("C has bigger perimeter",f)
else:
    print("C has bigger perimeter",f)
    print("B&A have same perimeter",d)
