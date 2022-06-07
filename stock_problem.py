import math
def maxProfitSUBARRAY(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = 0
    max_right = 0
    for i in range(mid, low-1 ,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def maxProfit(A, low, high):
    if high == low:
        return (low, high, A[low])
    else: 
        mid = math.floor((low + high) / 2)
        left_low, left_high, left_sum = maxProfit(A,low, mid)
        right_low, right_high, right_sum = maxProfit(A, mid+1, high)
        cross_low, cross_high, cross_sum = maxProfitSUBARRAY(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
price =  [-5, 8, 9, -6, 10, -15, 3]
n = len(price)
print(maxProfit(price, 0, n-1))