#Sum of two numbers

cont = 'yes'
while (cont=='yes' or cont == 'y'):

	if (cont=='no' or cont == 'n'):
		break
	num1 = int(raw_input("Enter 1st number: "))
	num2 = int(input("Enter 2nd number: "))

	sum = num1 + num2

	print("Sum of {0} and {1} = {2}".format(num1, num2,sum))
	
	cont = raw_input("Want to do again ? (y/n) ")
	
