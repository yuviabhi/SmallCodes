#Calculate area and perimeter of a triangle

import math

print ("Enter the sides of the triangle : ")
a = float(input("Enter side 1 : "))
b = float(input("Enter side 2 : "))
c = float(input("Enter side 3 : "))

if((a+b>c) and (b+c>a) and (c+a>b)):
	peri = a + b + c
	s = peri / 2
	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
	print ("Perimeter = {0}").format(peri)
	print ("Area = {0}").format(area)

else:
	
	print ("Triangle formation is impossible")


