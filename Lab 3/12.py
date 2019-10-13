def vol_rect_prism(height,width,depth):
    vol=height*width*depth
    return vol

h,w,d=input("Enter Height, Width, Depth")
res=vol_rect_prism(h,w,d)
print "Volume of Rectangular Prism",res
