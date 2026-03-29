def get_min_diff(arr, k):
    n = len(arr)
    if n == 1: return 0
    arr.sort()
    
    res = arr[-1] - arr[0]
    
    smallest = arr[0] + k
    largest = arr[-1] - k
    
    for i in range(n - 1):
        mi = min(smallest, arr[i+1] - k)
        ma = max(largest, arr[i] + k)
        if mi < 0: continue
        res = min(res, ma - mi)
        
    return res

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter tower heights: ").split()]
    k = int(input("Enter k: "))
    print(f"Minimum difference: {get_min_diff(arr, k)}")
