Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=input('Enter Value')
Enter Value20
>>> a
20
>>> a,b=input('Enter Two Values ')
Enter Two Values 20,9
>>> print a
20
>>> print b
9
>>> a=20
>>> b=3
>>> b=30
>>> if a==20:
	print a
else:
	print 'not 20'

	
20
>>> if a==20 and b>20:
	print a
elif a<20 and b>20:
	print b
else:
	print 'nothing'

	
20
>>> if a>0 or b<=0:
	print 'non zero'
elif b>=0 or a<10:
	print b
else:
	print a

	
non zero
>>> a=1
>>> while a<5:
	print 'a is smaller Demo'
	a=a+1

	
a is smaller Demo
a is smaller Demo
a is smaller Demo
a is smaller Demo
>>> 
