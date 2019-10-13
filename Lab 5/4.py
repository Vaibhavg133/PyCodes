a=[]
i=0
maxi=0
while i<10:
    print "Enter ",i+1," Elements "
    x=input()
    a.append(x)
    i=i+1
print "Before Reversing The List"
print a
print "After Reversing The List"
print a[::-1]
