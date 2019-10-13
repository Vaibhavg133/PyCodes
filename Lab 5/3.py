print "Enter Only 10 Inputs"
a=[]
i=0
while i<10:
    print "Enter Element ",i+1
    x=input()
    a.append(x)
    i=i+1

print "Elements Before Swapping"
print a
print "Elements after Swapping"
a[0],a[9]=a[9],a[0]
print a
