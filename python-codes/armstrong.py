#Check a number is armstrong or not !

num = int(input("Enter a number : "))
save = num
sum = 0
c = 0
while num>0 :
	num = num /10
	c=c+1
num = save
for i in range(0,c):
	num = num % 10
	sum = sum + num
	
if (sum == save) :
	print ("{0} is an  Armstrong no.").format(save)
else:
	print ("{0} is not an Armstrong no.").format(save)
	
