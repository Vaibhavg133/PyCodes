s = input("Enter a string : ")
c = 0 
for i in s :
    c += 1
    k = 1
    for j in s:
        if j==i :
            k+=1 
    if(k==2):
        print i
        break
    
