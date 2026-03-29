def sort_colors(nums):
    l, r = 0, len(nums) - 1
    i = 0
    
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter colors (0=Red, 1=White, 2=Blue): ").split()]
    sort_colors(nums)
    print(f"Sorted: {nums}")
