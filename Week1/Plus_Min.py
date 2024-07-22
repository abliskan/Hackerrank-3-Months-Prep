# ----- Type-1 ------
def plusMinus(arr):
    # Write your code here
    n=len(arr) 
    positive_ratio=0 
    negative_ratio=0 
    zero_ratio=0 
    for i in arr: 
        if i > 0: 
            positive_ratio += 1 
        elif i < 0: 
            negative_ratio += 1 
        else: 
            zero_ratio +=1 
            
    print(f"{positive_ratio/n}\n{negative_ratio/n}\n{zero_ratio/n}")

# ----- Type-2 ------
def plusMinus(arr):
    # Write your code here 
    positive_ratio, negative_ratio, zero_ratio = 0, 0, 0
    for i in range(0, (arr)): 
        if arr[i] > 0: 
            positive_ratio += 1 
        elif arr[i] < 0: 
            negative_ratio += 1 
        else: 
            zero_ratio +=1 
            
    print(f"{positive_ratio/len(arr)}\n{negative_ratio/len(arr)}\n{zero_ratio/len(arr)}")

# ----- Type-3 ------
def plusMinus(arr):
    # Write your code here - 1
    positive_ratio = 0
    negative_ratio = 0
    zero_ratio = 0
    
    # Write your code here - 2
    array_len = len(arr)
    
    for num in arr:
        if num > 0:
            positive_ratio += 1
        elif num < 0:
            negative_ratio += 1            
        elif num == 0:
            zero_ratio += 1
        else:
            return -1

    print(f"{positive_ratio/array_len:.6f}")
    print(f"{negative_ratio/array_len:.6f}")
    print(f"{zero_ratio/array_len:.6f}")