def volOfCylinder(hei,dia):
    rad=dia/2
    vol=3.14*rad*rad*hei
    return vol

heig,diam=input("Enter Height and Diameter")
res=volOfCylinder(heig,diam)
print "Volume of Cylinder : ",res
