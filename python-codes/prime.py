#Check a number is prime or not !

num = int(input("Enter a number : "))
flag = 0
for i in range(2,num/2):
	if(num%i != 0):
		flag = 1
		break
if(flag == 0):
	print ("{0} is not a prime no. ").format(num)
else:
	print ("{0} is a prime no. ").format(num)
		
	
