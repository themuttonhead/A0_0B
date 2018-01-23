#to_determine_biggest_area
a=float(input("enter the value of radius of the first circle:"))
b=float(input("enter the value of radius of the second circle:"))
c=3.1415
d=c*a**2
e=c*b**2
if d>e:
    print("first circle has bigger area",d)
else:
    print("second circle has bigger area",e)
