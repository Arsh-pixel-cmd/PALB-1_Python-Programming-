def can_place(nums, k, dist):
    count = 1
    last_pos = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - last_pos >= dist:
            count += 1
            last_pos = nums[i]
            if count == k:
                return True
    return False

def maximize_min_diff(nums, k):
    nums.sort()
    low = 0
    high = nums[-1] - nums[0]
    res = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place(nums, k, mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    k = int(input("Enter number of elements to select: "))
    print(f"Maximized minimum difference: {maximize_min_diff(arr, k)}")
