# ----- Type-1: use int var
def diagonalDifference(arr):
    # Write your code here
    n = len(arr[0])
    left_to_right = 0
    right_to_left = 0
    for i in range(n):
        left_to_right += arr[i][i]
        right_to_left += arr[i][n - 1 - i]
    return abs(right_to_left - left_to_right)

# ----- Type-2: use list var
def diagonalDifference(arr):
    # Write your code here
    left_to_right=[]
    right_to_left=[]
    for i in range(len(arr)):
        left_to_right.append(arr[i][i])
        right_to_left.append(arr[i - 1 + 1][len(arr) - i - 1])
    return (abs(sum(left_to_right)- sum(right_to_left)))
