def maxCrossingSum(A, low, mid, high):
	sum = 0
	left_sum = -10000
	for i in range(mid, low-1, -1):
		sum = sum + A[i]
		if (sum > left_sum):
			left_sum = sum
	sum = 0
	right_sum = -1000
	for i in range(mid + 1, high + 1):
		sum = sum + A[i]
		if (sum > right_sum):
			right_sum = sum
	return max(left_sum + right_sum, left_sum, right_sum)

def maxSubArraySum(A, low, high):
	if (low == high):
		return A[low]
	mid = (low + high) // 2
	return max(maxSubArraySum(A, low, mid),
			maxSubArraySum(A, mid+1, high),
			maxCrossingSum(A, low, mid, high))



def IterativeSum(a):
    maxprofit = 0
    minsofar = a[0]
    for i in range(0,len(a)):
        minsofar = min(minsofar,a[i])
        profit = a[i]-minsofar
        maxprofit = max(maxprofit,profit)
    return maxprofit


def subArraySum(A, A_len, maxsum):

	f1 = open("outputPS5.txt", "a")
	if maxsum<=0:
		str4="Day to buy: 1\nDay to sell: 1\n\n"
		f1.write(str4)
		return 1
	for i in range(A_len):
		curr_sum = A[i]
		j = i + 1
		while j <= n:
			if curr_sum == maxsum:
				str3 = "Day to buy:" + str(i+1) + "\nDay to sell:"+ str(j-1+2)+"\n\n"
				f1.write(str3)
				f1.close()
				return 1	
			if curr_sum > maxsum or j == n:
				break
			curr_sum = curr_sum + A[j]
			j += 1
	return 0

fp = open("inputPS5.txt", "r")
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
f = open("outputPS5.txt", "w")
max_sum = maxSubArraySum(res, 0, n-1)
if max_sum<0:
	str1="Maximum Profit (Divide & Conquer solution): 0\n"
else:
	str1="Maximum Profit (Divide & Conquer solution): "+ str(max_sum)+"\n"
f.write(str1)
f.close()
subArraySum(res, n, max_sum)
max_sum2=IterativeSum(price)
str2="Maximum Profit (Iterative solution): "+ str(max_sum2)+"\n"
f = open("outputPS5.txt", "a")
f.write(str2)
f.close()
subArraySum(res, n, max_sum2)

# Time Complexity for divide and conquer: maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation. 
# T(n) = 2T(n/2) + Θ(n) 
# Time Complexity : O(nlogn)