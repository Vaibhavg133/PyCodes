def reverse(s):
    newS = ""
    i = 1
    while(i<=len(s)):
        newS += s[-i]
        i+=1
    print newS
        
