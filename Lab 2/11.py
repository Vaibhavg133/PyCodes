sub1,sub2,sub3,sub4,sub5=input("Enter Marks obtained by student is 5 different Subject")
aggre=sub1+sub2+sub3+sub4+sub5
if aggre>500:
    print 'Error Occured'

else:
    perc=aggre/5

print aggre,' Marks out of 500 obtained by Student'
print perc,' % Obtained by Student'
