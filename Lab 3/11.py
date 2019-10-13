def area_rect_prism(height,depth,width):
    area=2*(height*depth+height*width+depth*width)
    return area

h,d,w=input("Enter Height, Depth, Weight    ")
res=area_rect_prism(h,d,w)
print "Area of rectangular prism ",res
