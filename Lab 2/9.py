a,b,c=input("Enter Three Numbers")
if a==b and b==c:
    print 'all are same'
elif a>b and a<c:
    print a,'  is greatest'
elif b>a and b>c:
    print b,'  is greatest'
else:
    print c,' is greatest'
