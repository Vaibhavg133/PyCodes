def area_cylinder(dia,hei):
    rad=dia/2
    area=2*3.14*rad*hei
    return area

diam,heig=input("Enter Diameter and Height    ")
res=area_cylinder(diam,heig)
print "Area =",res
