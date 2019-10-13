def prime(a):
    i = 2
    while(i<=a/2):
        if a%i==0 :
            return 1
        i+=1
    return 0

def check_prime(a):
    c = prime(a)
    return c


i = input("Enter a Number: ")
k = check_prime(i)
if(k==1):
    print "Not a prime number"
else :
    print "Prime Number"


    
