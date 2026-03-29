def jump_game_2(nums):
    res = 0
    l = r = 0
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter array (each element is max jump length): ").split()]
    print(f"Minimum jumps: {jump_game_2(nums)}")
