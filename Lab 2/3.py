print("  Enter Details for to compute Simple Interest")
principle=input("  Enter Principle Value : ")
rate=input("  Enter Rate : ")
time=input("  Enter Time : ")
SI=(principle*rate*time)/100
print " Simple Interest = ",SI
print " Amount after Simple Interest = ",SI+principle
print " Enter Details to calculate Compound Interest"
prin=input(" Enter The Value of Principle for Compound Interest")
r=input(" Enter The Value of Rate for Compound Interest ")
n=input(" Enter the value of n ")
t=input(" Enter the value of T for compound interest ")

I=prin*((1+(r/n)**n*t))-prin

print "Compound Interest = ",I




