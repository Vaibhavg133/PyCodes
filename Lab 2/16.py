large = 0
for x in range (0,10):
    num = input('Enter the number')
    if num % 2 !=0 and num > large:
        large = num

if large!=0:
    print 'Largest odd number is ' , large
else:
    print "No odd number found"
