#Calculate factorial of a number

num = int(input("Enter a number : "))
fact = 1
if num < 0:
	print ("Factorial of {0} is impossible since its a negative no.").format(num)
else:
	
	for i in range(1,num+1) :
		fact = fact * i
	
	print ("Factorial of {0} is {1}").format(num,fact)
