# adding 1 in all digits

num = input('Enter the number of 5 digits')
newnum = 0
n = 0
while num > 0:
    rem = num % 10
    if rem == 9:
        rem_new = -1
    else:
        rem_new = rem
    newnum = newnum + (rem_new + 1)* pow(10,n)
    num = num / 10
    n = n + 1

print 'new number is ' , newnum
