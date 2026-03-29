def find_3_sum(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            curr = nums[i] + nums[l] + nums[r]
            if curr == target:
                return True
            elif curr < target:
                l += 1
            else:
                r -= 1
    return False

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter array: ").split()]
    target = int(input("Enter target: "))
    print(f"Has triplet: {find_3_sum(nums, target)}")
