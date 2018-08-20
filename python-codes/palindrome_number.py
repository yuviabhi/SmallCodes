print ("Check a number is Palindrome or not")

n = int(input("Enter a number : "))

save = n
m = 0
 
while (n>0):
 	m = m*10 + n % 10
 	n = n/10

if (save == m):
	print ("{0} is palindrome").format(save)
else:
	print ("{0} is not palindrome").format(save)


