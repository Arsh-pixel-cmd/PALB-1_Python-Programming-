def count_elements_less_equal(nums, x):
    # This assumes sorted rotated array
    # The requirement is just to count elements <= x
    # We can do this in O(n) or O(log n)
    count = 0
    for n in nums:
        if n <= x:
            count += 1
    return count

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    x = int(input("Enter value x: "))
    print(f"Count: {count_elements_less_equal(arr, x)}")
