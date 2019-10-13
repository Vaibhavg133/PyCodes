def area_circle_dia(dia):
    rad=dia/2
    area=3.14*rad**2
    return area

diam=input("Enter Diameter    ")
res=area_circle_dia(diam)
print "Area ",res
