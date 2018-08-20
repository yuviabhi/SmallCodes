#Calculate power of a number using  RECURSION


def power_rec(x,n):
	if(n<1):
		return 1
	else :
		return x*power_rec(x,n-1)


if __name__=='__main__':
	num = int(input("Enter a number : "))
	power =  int(input("Enter value of power : "))

	print ("{0}^{1} is {2}").format(num,power,power_rec(num,power))
