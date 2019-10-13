def is_member(x,a):
    c = 0
    for i in a :
        if a[c:c+len(x)]==x:
            print "true"
            return
        c+=1
    print "false"
