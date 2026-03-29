def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter number array (each number appears twice except one): ").split()]
    print(f"Single number: {single_number(nums)}")
