def translate(s):
    newS = ""
    for i in s :
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            newS += i
        elif i == " " :
            newS += i 
        else :
            newS += i + "o" + i
    return newS
