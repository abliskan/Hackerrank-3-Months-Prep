# ----- Type-1 ------
def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if i == j:
                continue
            sum+=arr[j]
        if min == 0 and max == 0:
            min = sum
            max = sum
        if sum < min:
            min = sum
        if sum > max:
            max = sum
    print(min, max)

# ----- Type-2 ------
def miniMaxSum(arr):
    # Write your code here
    sum = 0
    minSum = 10
    maxSum = 0
    n = len(arr)
    for i in range(n):
        sum += arr[i]
        minSum = min(minSum, arr[i])
        maxSum = max(maxSum, arr[i])
    print(sum-maxSum, sum-minSum)

# ----- Type-3 ------
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum = 0
    for i in arr:
        sum += i
    print(sum-arr[4], sum-arr[0])