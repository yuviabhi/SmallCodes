#Calculate power of a number

num = int(input("Enter a number : "))
power =  int(input("Enter value of power : "))
cal = 1
for i in range(0,power):
	cal = cal*num
	
print ("{0}^{1} is {2}").format(num,power,cal)
