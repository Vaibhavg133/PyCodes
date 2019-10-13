def CeltoFah(cel):
    fah=1.8*cel+32
    return fah

celc=input("Enter Temperature in Celcius  ")
res=CeltoFah(celc)
print res," degree Fahrenheit"
