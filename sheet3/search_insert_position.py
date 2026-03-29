def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter sorted number array: ").split()]
    target = int(input("Enter target value: "))
    print(f"Index: {search_insert(nums, target)}")
