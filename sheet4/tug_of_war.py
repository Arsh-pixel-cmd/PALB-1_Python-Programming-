def tug_of_war(arr):
    n = len(arr)
    target_size = n // 2
    min_diff = float('inf')
    res_subsets = []
    
    total_sum = sum(arr)
    
    def backtrack(i, curr_subset, curr_sum):
        nonlocal min_diff, res_subsets
        
        if len(curr_subset) == target_size:
            diff = abs((total_sum - curr_sum) - curr_sum)
            if diff < min_diff:
                min_diff = diff
                res_subsets = [list(curr_subset), [x for x in arr if x not in curr_subset]] # Simple version
            return
            
        if i == n:
            return
            
        # Include arr[i]
        curr_subset.append(arr[i])
        backtrack(i + 1, curr_subset, curr_sum + arr[i])
        curr_subset.pop()
        
        # Exclude arr[i]
        backtrack(i + 1, curr_subset, curr_sum)

    backtrack(0, [], 0)
    return res_subsets

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    subsets = tug_of_war(arr)
    print(f"Divided subsets: {subsets}")
