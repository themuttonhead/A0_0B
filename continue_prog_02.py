#continue_prog_02
a=int(input("enter your range "))
b=int(input("enter the number to be omitted "))
for i in range(a):
    if i==b:
        continue
    print(i)
print("entered range is",a)
print("number omitted is",b)

