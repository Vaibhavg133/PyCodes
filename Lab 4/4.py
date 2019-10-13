def prime(a):
    i = 2
    while(i<=a/2):
        if a%i==0 :
            return 1
        i+=1
    return 0

def prime_btwn(a,b):
    i = a 
    while(i<=b):
        if(i%2 != 0):
            c = prime(i)
            if(c==0):
                print i
        i += 1

a,b = input("Enter two numbers(low to high): ")
print "Prime Between them are: "
prime_btwn(a,b)
 
        
