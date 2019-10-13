amount=input("Enter Amount : ")
rs100=0
rs50=0
rs10=0
rs100=amount/100
rs50=(amount%100)/50
rs10=(amount%50)/10
print amount,'  : Amount'
print 'Number of Rs. 100 Note : ',rs100
print 'Number of Rs. 50 Note : ',rs50
print 'Number of Rs. 10 Note : ',rs10
