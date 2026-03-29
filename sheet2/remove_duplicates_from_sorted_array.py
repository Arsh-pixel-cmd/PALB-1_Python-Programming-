def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter sorted number array (space separated): ").split()]
    k = remove_duplicates(nums)
    print(f"Number of unique elements: {k}")
    print(f"Modified array: {nums[:k]}")
