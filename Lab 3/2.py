def AreaTri():
    a,b,c=input("Enter 3 side of triangle  :   ")
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print area
    
AreaTri()
