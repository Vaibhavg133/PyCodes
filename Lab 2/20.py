a,b=input("Enter Both Numbers separated by comma: ")
i=1
while(i<=a and i<=b):
    if a%i==0 and b%i==0:
        c=i
    i=i+1
        
print c," is Greatest Common Divisor"

