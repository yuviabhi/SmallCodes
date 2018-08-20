print ("Reverse the digits of a number")

n = int(input("Enter a number : "))

save = n
m = 0
 
while (n>0):
 	m = m*10 + n % 10
 	n = n/10

print ("Reverse of {0} is {1}").format(save,m)
