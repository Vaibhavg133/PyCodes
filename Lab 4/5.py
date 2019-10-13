def max(a,b):
    if a>b :
        return a
    elif b>a :
        return b
    else :
        return "equal"

a,b = input("Enter two numbers: ")
new = max(a,b)
print new
