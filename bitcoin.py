def find_max_crossing_subarray(a,low,mid,high): 
	# compute the max sum from left half and right half of the array 
	# and return the overall maximum value with maxleft and max right indexes.
	lsum=-10000
	sum=0
	for i in range(mid, low-1, -1):
		sum = sum + a[i]

		if (sum > lsum):
			lsum = sum
			maxleft=i
	sum = 0
	rsum = -10000
	for j in range(mid + 1, high + 1):
		sum = sum + a[j]

		if (sum > rsum):
			rsum = sum
			maxright=j
	return (maxleft,maxright,lsum+rsum)

def find_maximum_subarray(a,low,high):
	# takes the array with its first and last index and 
	# if the array has only one value, it will return the index and value of it. 
	if high == low:
		return (low,high,a[low])
	else:
		mid=(low+high)//2 
		llow,lhigh,lsum=find_maximum_subarray(a,low,mid)  # for the first half of the array
		rlow,rhigh,rsum=find_maximum_subarray(a,mid+1,high)  # for the second half of the array
		clow,chigh,csum=find_max_crossing_subarray(a,low,mid,high) # for maximum subarray computation
	if lsum>=rsum and lsum>=csum:
		return (llow,lhigh,lsum)
	elif rsum>=lsum and rsum>=csum:
		return (rlow,rhigh,rsum)
	else:
		return (clow,chigh,csum)

def IterativeSum(a):
	# iterative approach to find the maximum profit with the start and the end day.
	maxprofit = 0
	minsofar = a[0]
	min_start = 0
	start = 0
	end =0
	for i in range(0,len(a)):
		if a[i]<=minsofar:
			min_start = i
		minsofar = min(minsofar,a[i])
		profit = a[i]-minsofar
		if maxprofit<profit:
			end = i
			start = min_start
		maxprofit = max(maxprofit,profit)
		
	return (start,end,maxprofit)

fp = open("inputPS5.txt", "r")
price=[]
days=[]
while True:
	lines = fp.readline()
	if lines == "":
		break
	price.append(int(lines.split("/")[1]))
	days.append(int(lines.split("/")[0]))
fp.close()
f = open("outputPS5.txt", "w")
day = days[0]
if len(price) == 1:
	str1="Maximum Profit (Divide & Conquer solution): 0 \nDay to buy:"+str(day)+" \nDay to sell:"+str(day)+"\n"
	f.write(str1)
	str2="Maximum Profit (Iterative solution): 0 \nDay to buy:"+str(day)+" \nDay to sell:"+str(day)+"\n"
	f.write(str2)
else:
	res = [price[i + 1] - price[i] for i in range(len(price)-1)]
	n = len(res)
	day_buy,day_sell,max_profit = find_maximum_subarray(res, 0, n-1)
	if max_profit<=0:
		str1="Maximum Profit (Divide & Conquer solution): 0 \nDay to buy:"+str(day)+" \nDay to sell:"+str(day)+"\n"
	else:
		str1="Maximum Profit (Divide & Conquer solution): "+ str(max_profit)+"\n"+"Day to buy:"+str(day_buy+day)+"\nDay to sell:"+str(day_sell+day+1)+"\n"
	f.write(str1)
	day_buy2,day_sell2,max_profit2=IterativeSum(price)
	if max_profit2<=0:
		str2="Maximum Profit (Iterative solution): 0 \nDay to buy:"+str(day)+" \nDay to sell:"+str(day)+"\n"
	else:
		str2="Maximum Profit (Iterative solution): "+ str(max_profit2)+"\n"+"Day to buy:"+str(day_buy2+day)+"\nDay to sell:"+str(day_sell2+day)+"\n"
	f = open("outputPS5.txt", "a")
	f.write(str2)
f.close()