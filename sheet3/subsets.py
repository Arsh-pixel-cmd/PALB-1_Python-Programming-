def subsets(nums):
    res = []
    subset = []
    
    def backtrack(i):
        if i >= len(nums):
            res.append(list(subset))
            return
            
        # Include nums[i]
        subset.append(nums[i])
        backtrack(i + 1)
        
        # Exclude nums[i]
        subset.pop()
        backtrack(i + 1)
        
    backtrack(0)
    return res

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter number array: ").split()]
    print(f"All subsets: {subsets(nums)}")
