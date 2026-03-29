def trap_rain_water(height):
    if not height: return 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    res = 0
    
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            res += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]
    return res

if __name__ == "__main__":
    heights = [int(x) for x in input("Enter heights: ").split()]
    print(f"Total water trapped: {trap_rain_water(heights)}")
