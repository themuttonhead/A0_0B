#function_prog_calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def mul(x,y):
    return x*y
def exp(x,y):
    return x**Y
def mod(x,y):
    return x%y
m=input("press c to calculate ")
m.lower()
while(m=="c"):
    a=int(input("enter your first value: "))
    b=int(input("enter your second value: "))
    i=input('''press 1 for addition, press 2 for subtraction, press 3 for division, press 4 for multiplication, press 5 for exponential or press 6 for modulus ''')
    if i=='''1''':
        print("addition")
        print(add(a,b))
    elif i=='''2''':
        print("subtraction")
        print(sub(a,b))
    elif i=='''3''':
        print("division")
        print(div(a,b))
    elif i=='''4''':
        print("multiplication")
        print(mul(a,b))
    elif i=='''5''':
        print("exponential")
        print(exp(a,b))
    elif i=='''6''':
        print("modulus")
        print(mod(a,b))
