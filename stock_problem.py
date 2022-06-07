
def maxCrossingSum(arr, l, m, h):

	# Include elements on left of mid.
	sm = 0
	left_sum = -10000

	for i in range(m, l-1, -1):
		sm = sm + arr[i]

		if (sm > left_sum):
			left_sum = sm

	# Include elements on right of mid
	sm = 0
	right_sum = -1000
	for i in range(m + 1, h + 1):
		sm = sm + arr[i]

		if (sm > right_sum):
			right_sum = sm

	# Return sum of elements on left and right of mid
	# returning only left_sum + right_sum will fail for [-2, 1]
	return max(left_sum + right_sum, left_sum, right_sum)


# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):

	# Base Case: Only one element
	if (l == h):
		return arr[l]

	# Find middle point
	m = (l + h) // 2

	# Return maximum of following three possible cases
	# a) Maximum subarray sum in left half
	# b) Maximum subarray sum in right half
	# c) Maximum subarray sum such that the
	#	 subarray crosses the midpoint
	return max(maxSubArraySum(arr, l, m),
			maxSubArraySum(arr, m+1, h),
			maxCrossingSum(arr, l, m, h))



def KadaneSum(a,size):
	
	max_so_far = -10000
	max_ending_here = 0
	
	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return max_so_far


def subArraySum(arr, n, sum_):
	
	# Pick a starting
	# point
	for i in range(n):
		curr_sum = arr[i]
	
		# try all subarrays
		# starting with 'i'
		j = i + 1
		f1 = open("outputPS5.txt", "a")
		while j <= n:
		
			if curr_sum == sum_:
				str3 = "Day to buy:" + str(i+1) + "\nDay to sell:"+ str(j-1+2)+"\n\n"
				f1.write(str3)
				f1.close
				return 1
				
			if curr_sum > sum_ or j == n:
				break
			
			curr_sum = curr_sum + arr[j]
			j += 1

	print ("No subarray found")
	return 0

fp = open("inputPS5.txt", "r")
f =open("outputPS5.txt", 'r+') 
f.truncate(0)
f.close()
day_number=0
price=[]
while True:
    lines = fp.readline()
    if lines == "":
        break
    day_number=day_number+1
    price.append(int(lines.split("/")[1]))
fp.close()
res = [price[i + 1] - price[i] for i in range(len(price)-1)]
n = len(res)
f = open("outputPS5.txt", "a")
max_sum = maxSubArraySum(res, 0, n-1)
str1="Maximum Profit (Divide & Conquer solution): "+ str(max_sum)+"\n"
f.write(str1)
f.close()
subArraySum(res, n, max_sum)
max_sum2=KadaneSum(res,n)
str2="Maximum Profit (Iterative solution): "+ str(max_sum2)+"\n"
f = open("outputPS5.txt", "a")
f.write(str2)
f.close()
subArraySum(res, n, max_sum2)


# Time Complexity for divide and conquer: maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation. 
# T(n) = 2T(n/2) + Θ(n) 
# Time Complexity : O(nlogn)