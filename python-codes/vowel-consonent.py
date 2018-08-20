#Check vowel or consonent

ch = raw_input("Enter an alphabet : ")

if (len(ch) > 0 and len(ch) < 2):
	ch = ch.upper()
	if (ch=='A' or ch=='E' or ch=='I'or ch=='O'or ch=='U'):
		print ("{0} is vowel").format(ch)
	else:
		print ("{0} is consonent").format(ch)
else:	
	print ("Enter one alphabet only")
	

