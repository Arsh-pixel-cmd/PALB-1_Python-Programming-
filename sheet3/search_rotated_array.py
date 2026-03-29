def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
            
        # Left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # Right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter rotated sorted array: ").split()]
    target = int(input("Enter target: "))
    print(f"Index: {search_rotated(nums, target)}")
