#Calculating compond interest

def ci():
    p = input('Ente principal value')
    r = input('Enter the rate')
    t = input('Enter the time')

    a = p * pow(1+(r/100.0),t)
    print 'Compound interest is:', a

ci()
