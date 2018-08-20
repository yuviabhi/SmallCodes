print ("Reverse a string")

def reverse_str(l):
	if len(l) < 1:
		return l
	else:
		return (reverse_str(l[1:]) + l[0])



s = raw_input("Enter a string : ")
print ("Reverse of {0} is {1}").format(s, reverse_str(s))
