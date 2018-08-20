print ("Check a string is palindrome or not")

def reverse_str(l):
	if len(l) < 1:
		return l
	else:
		return (reverse_str(l[1:]) + l[0])



s = raw_input("Enter a string : ")
if s == reverse_str(s) :
	print ("{0} is palindrome").format(s)
else:
	print ("{0} is not palindrome").format(s)
