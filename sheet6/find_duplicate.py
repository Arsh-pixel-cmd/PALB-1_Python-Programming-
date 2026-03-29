def find_duplicate(nums):
    # Floyd's Tortoise and Hare (Cycle Detection)
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter array (n+1 integers in range [1, n]): ").split()]
    print(f"Duplicate number: {find_duplicate(nums)}")
