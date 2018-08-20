#Calculate factorial of a number using Recursions

def facto(n):
	if n<1 :
		return 1
	else:
		return n*facto(n-1)
		
if __name__ == '__main__':	
	num = int(input("Enter a number : "))

	if(num<0):
		print 'Impossible since its a negative no.'
	else :
		print ("Factorial of {0} is {1}").format(num,facto(num))

