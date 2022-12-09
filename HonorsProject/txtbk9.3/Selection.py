from sys import argv, exit

DEFAULT_VAL = 5

# implementation of worst case
# linear time algorithm to find
# k'th smallest element

# Read integers from the given filename.
#
# Return value: list of integers
def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")


# Returns k'th smallest element in arr[l..r]
# in worst case linear time.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
def kthSmallest(arr, l, r, k):
	
	# If k is smaller than number of
	# elements in array
	if (k > 0 and k <= r - l + 1):
		
		# Number of elements in arr[l..r]
		n = r - l + 1

		# Divide arr[] in groups of size 5,
		# calculate median of every group
		# and store it in median[] array.
		median = []

		i = 0
		while (i < n // DEFAULT_VAL):
			median.append(findMedian(arr, l + i * DEFAULT_VAL, DEFAULT_VAL))
			i += 1

		# For last group with less than 5 elements
		if (i * 5 < n):
			median.append(findMedian(arr, l + i * DEFAULT_VAL,
											n % DEFAULT_VAL))
			i += 1

		# Find median of all medians using recursive call.
		# If median[] has only one element, then no need
		# of recursive call
		if i == 1:
			medOfMed = median[i - 1]
		else:
			medOfMed = kthSmallest(median, 0,
								i - 1, i // 2)

		# Partition the array around a medOfMed
		# element and get position of pivot
		# element in sorted array
		pos = partition(arr, l, r, medOfMed)

		# If position is same as k
		if (pos - l == k - 1):
			return arr[pos]
		if (pos - l > k - 1): # If position is more,
							# recur for left subarray
			return kthSmallest(arr, l, pos - 1, k)

		# Else recur for right subarray
		return kthSmallest(arr, pos + 1, r,
						k - pos + l - 1)

	# If k is more than the number of
	# elements in the array
	return 999999999999

def swap(arr, a, b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

# It searches for x in arr[l..r],
# and partitions the array around x.
def partition(arr, l, r, x):
	for i in range(l, r):
		if arr[i] == x:
			swap(arr, r, i)
			break

	x = arr[r]
	i = l
	for j in range(l, r):
		if (arr[j] <= x):
			swap(arr, i, j)
			i += 1
	swap(arr, i, r)
	return i

# A simple function to find
# median of arr[] from index l to l+n
def findMedian(arr, l, n):
	lis = []
	for i in range(l, l + n):
		lis.append(arr[i])
		
	# Sort the array
	lis.sort()

	# Return the middle element
	return lis[n // 2]

def makeRandArray():
    randArray = []
    
    print(randArray)
    

# Driver Code
if __name__ == '__main__':
    arr = []
    k = 0
    
    if len(argv) != 3 :
        # exit("usage: python3 "+argv[0]+" datafile")
        arr = makeRandArray()
        k = 3
    else:
        arr = read_array(argv[1])
        k = read_array(argv[2])
        
	n = len(arr)
    print("K'th smallest element is",kthSmallest(arr, 0, n - 1, k))
