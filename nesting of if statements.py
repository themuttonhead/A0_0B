#nesting_of_if
a=int(input("enter a number between 1 to 10: "))
if a%2==0:
    print("its even")
    if a==2:
        print("its even prime number")
    else:
        if a==4:
            print("the root is 2")
            print("or the roor is -2")
else:
    print("its odd")
    if a==1:
        print("neither prime nor composite")
    else:
        if a==9:
            print("the root is 3")
            print("or the root is -3")
