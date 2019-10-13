def SimpleInterest():
    prin,time,rate=input("Enter Principle, Rate, Time  : ")
    si=(prin*time*rate)/100
    print "Simple Interest is ",si
    print 'Total Amount is ',prin+si

SimpleInterest()
