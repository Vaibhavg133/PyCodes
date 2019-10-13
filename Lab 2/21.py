a,b=input(" Enter Two Numbers ")
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        c=i
    i=i+1
lcm=(a*b)/c
print "  LCM =",lcm 

