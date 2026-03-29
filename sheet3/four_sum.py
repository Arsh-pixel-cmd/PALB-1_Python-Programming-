def four_sum(nums, target):
    nums.sort()
    res = []
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            
            l, r = j + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[j] + nums[l] + nums[r]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
    return res

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter nums: ").split()]
    target = int(input("Enter target: "))
    print(f"Quadruplets: {four_sum(nums, target)}")
