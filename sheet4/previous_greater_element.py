def previous_greater_element(arr):
    stack = []
    pge = []
    for x in arr:
        while stack and stack[-1] <= x:
            stack.pop()
        pge.append(stack[-1] if stack else -1)
        stack.append(x)
    return pge

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    print(f"PGE: {previous_greater_element(arr)}")
