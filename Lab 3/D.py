#string as a parameter

s = raw_input('Enter a string')

length =len(s)
x = 0
while (length > 0):
    print s[x],
    print ' ',
    x = x + 1
    length = length - 1
