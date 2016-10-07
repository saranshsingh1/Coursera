with open("IntegerArray.txt", 'r') as f:
	array = [int(i.strip()) for i in f.readlines()]

count = 0
def mergesort(array):
	'''Divide the list to sort the elements'''
	if len(array) < 2:
		return array

	mid = len(array) // 2
	left = array[ : mid]
	right = array[mid : ]

	#Divide the list into sub-lists of left and right
	#till one element per array
	left = mergesort(left)
	right = mergesort(right)

	return list(merge(left, right))

def merge(l, r):
	'''Merge the sorted list'''
	res = []
	i, j = 0, 0
	global count

	while i < len(l) and j < len(r):
		if l[i] <= r[j]:
			res.append(l[i])
			i += 1
			#Add the remaning elements if left array empty
			if i == len(l) and j != len(r):
				res.extend(r[j:])
		else:
			res.append(r[j])
			j += 1

			#Count the number of inversions
			count += (len(l) - i)

			#Add the remaning elements if right array empty
			if j == len(r) and i != len(l):
				res.extend(l[i:])
	return res


print mergesort(array)
print count
