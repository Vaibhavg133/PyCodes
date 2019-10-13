def facto(num):
    fact=1
    while(num>0):
        fact=fact*num
        num=num-1
    return fact

num=input("Enter Number")
z=facto(num)
print z
