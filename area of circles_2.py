#to_determine_biggest_area
a=float(input("enter the value of radius of the first circle:"))
b=float(input("enter the value of radius of the second circle:"))
c=3.1415
d=c*a**2
e=c*b**2
if d>e:
    print("first circle has bigger area by",d-e)
    print("the area of first circle is",d)
if d==e:
    print("both the areas are same")
    print("the area is",d)
else:    
    print("second circle has bigger area by",e-d)
    print("the area of second circle is",e)
