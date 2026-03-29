def search_range(nums, target):
    def find_bound(is_left):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if is_left:
                    r = m - 1
                else:
                    l = m + 1
        return i
        
    return [find_bound(True), find_bound(False)]

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter sorted number array: ").split()]
    target = int(input("Enter target: "))
    print(f"Range: {search_range(nums, target)}")
