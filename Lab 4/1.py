minSaving = 0 
minCurrent = 0

def saving(amount):
    global minSaving 
    global minCurrent
    if((minSaving - amount)<1000):
        print "Minimum amount of 1000 required for the transaction "
    else:
        minSaving -= amount
        print "Transcation Success"
    return

def current(amount):
    global minSaving
    global minCurrent
    if((minCurrent - amount)<10000):
        print "Minimum amount of 10000 required for the transaction "
    else:
        minCurrent -= amount
        print "Transcation Success"
    return


i = 1
while(i):
    account = input("Enter bank account:\n1)Saving\n2)Current\n")
    action = input("Enter \n1)Withdrawal\n2)Deposite\n")
    if(account==1 and action==1):
        withdrawal = input("Enter amount: ")
        saving(withdrawal)
    elif(account==1 and action==2):
        deposite = input("Enter amount: ")
        minSaving += deposite
    elif(account==2 and action==1):
        withdrawal = input("Enter amount: ")
        current(withdrawal)
    elif(account==2 and action==2):
        deposite = input("Enter amount: ")
        minCurrent += deposite
    i = input("To continue PRESS 1\nAbort Transaction PRESS 0\n")
    
    
