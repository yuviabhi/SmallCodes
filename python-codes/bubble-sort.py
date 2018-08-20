#Bubble sort


list1 = []
n = int(raw_input('How many numbers ? '))

def remove_duplicates(l):
    return list(set(l))

for num in range(0,n) :
	print ('Enter no. {0} :').format(num+1)
	list1.append(raw_input())
	
print 'Before sorting : ', list1

list1 = remove_duplicates(list1)
n = len(list1)

for i in range(0,n):
	for j in range(0,n-i-1) :
		if( list1[j] > list1[j+1] ):
			temp = list1[j]
			list1[j]=list1[j+1]
			list1[j+1] = temp
			
print 'After sorting : ', list1
