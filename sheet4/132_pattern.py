def find132pattern(nums):
    stack = [] # pair [num, currMin], mono-decreasing
    currMin = nums[0]
    
    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True
        stack.append([n, currMin])
        currMin = min(currMin, n)
    return False

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    print(f"Contains 132 pattern: {find132pattern(arr)}")
