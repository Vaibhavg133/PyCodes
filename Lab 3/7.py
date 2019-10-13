def fahToCel(fah):
    cel=((fah-32)*5)/9
    return cel

fahr=input("Enter Temperature in Fahrenheit  ")
res=fahToCel(fahr)
print res," degree Celcuis"
