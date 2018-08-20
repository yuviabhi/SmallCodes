#Print the pattern
'''
1 2 3 ... n
1 2 3 ... n
1 2 3 ... n
1 2 3 ... n
'''

n = int(input("How many lines ?  "))

for i in range(1,n+1):
	for j in range(1,n+1):
		print (" {0}").format(i+j-1),
	print("")
